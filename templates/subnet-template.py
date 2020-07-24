"""Creates the Subnet"""
# https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks


def GenerateConfig(context):

    resources = []
    for i in context.properties['subnets']:
        base_name = context.env['deployment'] + \
            '-' + i['vpc'] + '-' + context.env['name']
        resources.append({
            'name': base_name,
            'type': 'compute.v1.subnetwork',
            'properties': {
                'network': '$(ref.' + context.env['deployment'] + '-' + i['vpc'] + '.selfLink)',
                'ipCidrRange': i['ipCidrRange'],
                'region': i['region']
            }
        })

    return {'resources': resources}
