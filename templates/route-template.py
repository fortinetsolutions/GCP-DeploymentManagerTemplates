"""Creates the route."""
# https://cloud.google.com/compute/docs/reference/rest/v1/routes

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']
    resources = [{
        'name': base_name,
        'type': 'compute.v1.routes',
        'properties': {
            'network': ''.join(['projects/', context.env['project'], '/global/networks/', context.env['deployment'], 'vpc']),
            'destRange': context.properties['destRange'],
            'priority': context.properties['priority'],
            'nextHopIp': context.properties['nextHopIp']
        }
    }]

    return {'resources': resources}
