"""Creates the Forwarding Rules."""
# https://cloud.google.com/compute/docs/reference/rest/v1/forwardingRules


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    resources = [{
        'name': base_name,
        'type': 'compute.v1.forwardingRules',
        'properties': {
            'region': context.properties['region'],
            'target': '$(ref.' + context.env['deployment'] + '-target-instance'+'.selfLink)',
            'IPAddress': '$(ref.' + context.env['deployment'] + '-static-ip'+'.selfLink)',
            'IPProtocol': context.properties['ipProtocol']
        }
    }]

    return {'resources': resources}
