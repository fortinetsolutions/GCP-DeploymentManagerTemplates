"""Creates the firewall."""
# https://cloud.google.com/compute/docs/reference/rest/v1/firewalls


def GenerateConfig(context):

    resources = []
    for i in context.properties['vpcs']:
        base_name = context.env['deployment'] + \
            '-' + i + '-' + context.env['name']
        resources.append({
            'name': base_name + '-ingress',
            'type': 'compute.v1.firewall',
            'properties': {
                'network': '$(ref.' + context.env['deployment'] + '-' + i + '.selfLink)',
                'sourceRanges': ['0.0.0.0/0'],
                'allowed': [{
                    'IPProtocol': 'all',
                    'ports': []
                }]
                # 'allowed': [{
                #     'IPProtocol': 'TCP',
                #     'ports': [22, 80, 443]
                # }, {
                #     'IPProtocol': 'ICMP',
                #     'ports': []
                # }]
            }
        })
        resources.append({
            'name': base_name + '-egress',
            'type': 'compute.v1.firewall',
            'properties': {
                'network': '$(ref.' + context.env['deployment'] + '-' + i + '.selfLink)',
                'direction': 'EGRESS',
                'destinationRanges': ['0.0.0.0/0'],
                'allowed': [{
                    'IPProtocol': 'all',
                    'ports': []
                }]
            }
        })
    return {'resources': resources}
