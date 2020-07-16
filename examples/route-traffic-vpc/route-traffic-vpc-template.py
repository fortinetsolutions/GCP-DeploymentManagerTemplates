"""Creates a Compute Engine with Fortigate Instance, VPC, Subnet, Firewall, Static IP, Target Instance, Forwarding Rules."""


def GenerateConfig(context):

    resources = [{
        'name': 'fgt-instance',
        'type': '../../templates/fgt-instance-template.py',
        'properties': {
            'image': '<FORTIGATE_VM_IMAGE>',
            'machineType': 'n1-standard-1',
            'metadata-from-file': {
                'license': 'license.lic',
                'user-data': 'byol'
            },
            'zone': 'us-central1-a'
        }
    }, {
        'name': 'nginx-instance',
        'type': '../../templates/nginx-instance-template.py',
        'properties': {
            'image': 'ubuntu-os-cloud/global/images/family/ubuntu-1804-lts',
            'machineType': 'n1-standard-1',
            'metadata-from-file': {
                'user-data': 'nginx'
            },
            'zone': 'us-central1-a'
        }
    }, {
        'name': 'vpc',
        'type': '../../templates/vpc-template.py'
    }, {
        'name': 'subnet',
        'type': '../../templates/subnet-template.py',
        'properties': {
            'ipCidrRange': '172.18.0.0/24',
            'region': 'us-central1'
        }
    }, {
        'name': 'firewall',
        'type': '../../templates/firewall-template.py'
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
