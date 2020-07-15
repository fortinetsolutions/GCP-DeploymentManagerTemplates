"""Creates the firewall."""


def GenerateConfig(context):

    base_name = context.env['deployment'] + '-' + context.env['name']

    resources = [{
        'name': base_name,
        'type': 'compute.v1.firewall',
        'properties': {
            'network': '$(ref.' + context.env['deployment'] + '-vpc'+'.selfLink)',
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
    }]
    return {'resources': resources}
