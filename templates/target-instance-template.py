"""Creates the Target Instance."""
# https://cloud.google.com/compute/docs/reference/rest/v1/targetInstances


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    resources = [{
        'name': base_name,
        'type': 'compute.v1.targetInstances',
        'properties': {
            'instance': '$(ref.' + context.env['deployment'] + context.properties['instance'] + '.selfLink)',
            'zone': context.properties['zone']
        }
    }]
    return {'resources': resources}
