"""Creates a Compute Engine with Ubuntu Instance with nginx installed, VPC, Subnet and Firewall."""


def GenerateConfig(context):

    resources = [{
        'name': 'instance',
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
        'type': '../../templates/subnet-template.py'
    }, {
        'name': 'firewall',
        'type': '../../templates/firewall-template.py'
    }]

    return {'resources': resources}
