"""Creates FortiGate Instance."""
# https://cloud.google.com/compute/docs/reference/rest/v1/instances

import six

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    # Metadata
    items = []
    for key, value in six.iteritems(context.properties['metadata-from-file']):
        items.append({
            'key': key,
            'value': context.imports[value]
        })
    metadata = {'items': items}

    # VPCs
    vpcs = []
    for i in context.properties['vpcs']:
        vpcs.append({
            'network': '$(ref.' + context.env['deployment'] + '-' + i['vpc'] + '.selfLink)',
            'subnetwork': '$(ref.' + context.env['deployment'] + '-' + i['subnet'] + '.selfLink)',
            'accessConfigs': i['accessConfigs']
        })

    instance = {
        'canIpForward': context.properties['canIpForward'],
        'zone': context.properties['zone'],
        'machineType': ''.join([COMPUTE_URL_BASE, 'projects/', context.env['project'],
                                '/zones/', context.properties['zone'],
                                '/machineTypes/', context.properties['machineType']]),
        'disks': [{
            'deviceName': 'boot',
            'type': 'PERSISTENT',
            'boot': True,
            'autoDelete': True,
            'initializeParams': {
                    'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/', context.env['project'], '/global/images/',
                                            context.properties['image']])
            }
        }],
        'metadata': metadata,
        'serviceAccounts': context.properties['serviceAccounts'],
        'networkInterfaces': vpcs
    }

    # Resources to return.
    resources = {
        'resources': [{
            'name': base_name,
            'type': 'compute.v1.instance',
            'properties': instance
        }]
    }
    return resources
