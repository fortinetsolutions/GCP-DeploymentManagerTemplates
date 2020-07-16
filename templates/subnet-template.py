"""Creates the Subnet"""
# https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    resources = [{
        'name': base_name,
        'type': 'compute.v1.subnetwork',
        'properties': {
            'network': '$(ref.' + context.env['deployment'] + '-vpc'+'.selfLink)',
            'ipCidrRange': context.properties['ipCidrRange'],
            'region': context.properties['region']
        }
    }]
    return {'resources': resources}
