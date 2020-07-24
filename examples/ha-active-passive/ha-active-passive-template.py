"""Creates 2 FortiGate Instances (active and passive) with 4 VPCs, 4 Subnets, External IP and Internal Route."""

import six

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):

    passive_items = []
    for key, value in six.iteritems(context.properties['metadata-from-file-passive']):
        passive_items.append({
            'key': key,
            'value': context.imports[value]
        })
    passive_metadata = {'items': passive_items}

    resources = [{
        'name': 'fgt-active-instance',
        'type': '../../templates/fgt-instance-template.py',
        'properties': {
            'canIpForward': context.properties['canIpForward'],
            'machineType': context.properties['machineType'],
            'image': context.properties['image'],
            'zone': context.properties['zone'],
            'metadata-from-file': context.properties['metadata-from-file-active'],
            'vpcs': [{
                'vpc': 'public-vpc',
                'subnet': 'public-vpc-subnet',
                'accessConfigs': [{
                    'natIP': '$(ref.' + context.env['deployment'] + '-static-ip.address)',
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT',
                    'networkTier': 'PREMIUM'
                }]}, {
                'vpc': 'private-vpc',
                'subnet': 'private-vpc-subnet',
                'accessConfigs': []},
                {
                'vpc': 'ha-vpc',
                'subnet': 'ha-vpc-subnet',
                'accessConfigs': []},
                {
                'vpc': 'mgmt-vpc',
                'subnet': 'mgmt-vpc-subnet',
                'accessConfigs': [{
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT'
                }]}
            ]
        }
    }, {
        'name': context.env['deployment'] + '-fgt-passive-instance',
        'type': 'compute.v1.instance',
        'properties': {
            'canIpForward': context.properties['canIpForward'],
            'zone': context.properties['zone'],
            'machineType': ''.join([COMPUTE_URL_BASE, 'projects/', context.env['project'],
                                    '/zones/', context.properties['zone'], '/machineTypes/', context.properties['machineType']]),
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
            'metadata': passive_metadata,
            'networkInterfaces': [{
                'network': '$(ref.' + context.env['deployment'] + '-public-vpc.selfLink)',
                'subnetwork': '$(ref.' + context.env['deployment'] + '-public-vpc-subnet.selfLink)',
                'accessConfigs': []
            }, {
                'network': '$(ref.' + context.env['deployment'] + '-private-vpc.selfLink)',
                'subnetwork': '$(ref.' + context.env['deployment'] + '-private-vpc-subnet.selfLink)',
                'accessConfigs': []
            }, {
                'network': '$(ref.' + context.env['deployment'] + '-ha-vpc.selfLink)',
                'subnetwork': '$(ref.' + context.env['deployment'] + '-ha-vpc-subnet.selfLink)',
                'accessConfigs': []
            }, {
                'network': '$(ref.' + context.env['deployment'] + '-mgmt-vpc.selfLink)',
                'subnetwork': '$(ref.' + context.env['deployment'] + '-mgmt-vpc-subnet.selfLink)',
                'accessConfigs': [{
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT'
                }]
            }]
        },
        'metadata': {
            'dependsOn': [''.join([context.env['deployment'], '-fgt-active-instance'])]
        }
    }, {
        'name': context.env['deployment'] + '-route',
        'type': 'compute.v1.routes',
        'properties': {
            'network': ''.join(['projects/', context.env['project'], '/global/networks/', context.env['deployment'], '-private-vpc']),
            'destRange': context.properties['destRange'],
            'priority': context.properties['priority'],
            'nextHopIp': context.properties['nextHopIp']
        },
        'metadata': {
            'dependsOn': [''.join([context.env['deployment'], '-fgt-active-instance'])]
        }
    }]
    return {'resources': resources}
