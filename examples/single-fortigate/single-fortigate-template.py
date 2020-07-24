"""Creates a Compute Engine with Fortigate Instance, VPC, Subnet and Firewall."""

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):

    resources = [{
        'type': 'compute.v1.disk',
        'name': context.env['deployment'] + '-log-disk',
        'properties': {
            'zone': context.properties['zone'],
            'sizeGb': 30,
            'type': ''.join([COMPUTE_URL_BASE, 'projects/',
                             context.env['project'], '/zones/',
                             context.properties['zone'],
                             '/diskTypes/pd-standard'])
        }
    }, {
        'name': 'instance',
        'type': '../../templates/fgt-instance-template.py',
        'properties': {
            'canIpForward': context.properties['canIpForward'],
            'machineType': context.properties['machineType'],
            'image': context.properties['image'],
            'metadata-from-file': {
                'license': 'license.lic',
                'user-data': 'byol'
            },
            'zone': context.properties['zone'],
            'vpcs': [{'vpc': 'public-vpc',
                      'subnet': 'public-vpc-subnet',
                      'accessConfigs': [{
                          'name': 'External NAT',
                          'type': 'ONE_TO_ONE_NAT'
                      }]},
                     {'vpc': 'private-vpc',
                      'subnet': 'private-vpc-subnet',
                      'accessConfigs': []}
                     ]
        }
    }]

    return {'resources': resources}
