"""Creates a Compute Engine with Fortigate Instance, VPC, Subnet, Firewall, Static IP, Target Instance, Forwarding Rules."""


def GenerateConfig(context):

    resources = [{
        'name': 'fgt-instance',
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
    }, {
        'name': 'nginx-instance',
        'type': '../../templates/nginx-instance-template.py',
        'properties': {
            'image': 'ubuntu-os-cloud/global/images/family/ubuntu-1804-lts',
            'machineType': context.properties['machineType'],
            'metadata-from-file': {
                'user-data': 'nginx'
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
    }, {
        'name': 'static-ip',
        'type': '../../templates/static-ip-template.py',
        'properties': {
            'region': 'us-central1'
        }
    }, {
        'name': 'target-instance',
        'type': '../../templates/target-instance-template.py',
        'properties': {
            'instance': '-fgt-instance',
            'zone': 'us-central1-a'
        }
    }, {
        'name': 'forwarding-rules-tcp',
        'type': '../../templates/forwarding-rules-template.py',
        'properties': {
            'region': 'us-central1',
            'ipProtocol': 'TCP'
        }
    }, {
        'name': 'forwarding-rules-udp',
        'type': '../../templates/forwarding-rules-template.py',
        'properties': {
            'region': 'us-central1',
            'ipProtocol': 'UDP'
        }
    }]

    return {'resources': resources}
