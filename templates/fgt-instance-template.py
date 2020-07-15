"""Creates FortiGate Instance."""
import six

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    items = []
    for key, value in six.iteritems(context.properties['metadata-from-file']):
        items.append({
            'key': key,
            'value': context.imports[value]
        })
    metadata = {'items': items}

    instance = {
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
                    'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/', context.env['project'],
                                            context.properties['image']])
            }
        }],
        'metadata': metadata,
        'networkInterfaces': [{
            'network': '$(ref.' + context.env['deployment'] + '-vpc'+'.selfLink)',
            'subnetwork': '$(ref.' + context.env['deployment'] + '-subnet'+'.selfLink)',
            'accessConfigs': [{
                'name': 'External NAT',
                'type': 'ONE_TO_ONE_NAT'
            }]
        }]
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
