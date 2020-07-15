"""Creates the Subnet"""


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    resources = [{
        'name': base_name,
        'type': 'compute.v1.subnetwork',
        'properties': {
            'ipCidrRange': '172.18.0.0/24',
            'network': '$(ref.' + context.env['deployment'] + '-vpc'+'.selfLink)',
            'region': 'us-central1'
        }
    }]
    return {'resources': resources}
