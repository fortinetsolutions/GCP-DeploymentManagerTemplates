"""Creates the VPC Networks."""


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    resources = [{
        'name': base_name,
        'type': 'compute.v1.network',
        'properties': {
            'autoCreateSubnetworks': False,
        }
    }]
    return {'resources': resources}
