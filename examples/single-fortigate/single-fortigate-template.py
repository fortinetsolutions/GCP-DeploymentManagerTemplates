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
            'image': context.properties['image'],
            'machineType': context.properties['machineType'],
            'metadata-from-file': {
                'license': 'license.lic',
                'user-data': 'byol'
            },
            'serviceAccounts': [{
                'email': context.properties['serviceAccountEmail'],
                'scopes': context.properties['scopes']
            }],
            'vpcs': [{'vpc': 'public-vpc',
                      'subnet': 'public-vpc-subnet',
                      'accessConfigs': [{
                          'name': 'External NAT',
                          'type': 'ONE_TO_ONE_NAT'
                      }]},
                     {'vpc': 'private-vpc',
                      'subnet': 'private-vpc-subnet',
                      'accessConfigs': []}
                     ],
            'zone': context.properties['zone'],
        }
    }]

    return {'resources': resources}
