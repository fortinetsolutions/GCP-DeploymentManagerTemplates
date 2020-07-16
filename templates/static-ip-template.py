"""Creates the External IP."""
# https://cloud.google.com/compute/docs/reference/rest/v1/addresses


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    resources = [{
        'name': base_name,
        'type': 'compute.v1.addresses',
        'properties': {
            'region': context.properties['region']
        }
    }]
    return {'resources': resources}
