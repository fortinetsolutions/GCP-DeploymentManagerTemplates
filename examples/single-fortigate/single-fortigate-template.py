"""Creates a Compute Engine with Fortigate Instance, VPC, Subnet and Firewall."""


def GenerateConfig(context):

    resources = [{
        'name': 'instance',
        'type': '../../templates/fgt-instance-template.py',
        'properties': {
            'image': '/global/images/skc-fgt-vm-image',
            'machineType': 'n1-standard-1',
            'metadata-from-file': {
                'license': 'license.lic',
                'user-data': 'byol'
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
