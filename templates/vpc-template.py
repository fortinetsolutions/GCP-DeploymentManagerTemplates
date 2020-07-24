"""Creates the VPC Networks."""
# https://cloud.google.com/compute/docs/reference/rest/v1/networks


def GenerateConfig(context):

    resources = []
    for i in context.properties['vpcs']:
        base_name = context.env['deployment'] + \
            '-' + i + '-' + context.env['name']
        resources.append({
            'name': base_name,
            'type': 'compute.v1.network',
            'properties': {
                'autoCreateSubnetworks': False
            }
        })

    return {'resources': resources}
