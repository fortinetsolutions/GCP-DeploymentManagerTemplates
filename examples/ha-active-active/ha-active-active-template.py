
import six

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):

    resources = [{
        'name': context.env['deployment'] + '-hc-mig',
        'type': 'compute.v1.healthCheck',
        'properties': {
            'type': 'HTTPS',
            'checkIntervalSec': context.properties['autohealingCheckIntervalSec'],
            'timeoutSec': context.properties['autohealingTimeoutSec'],
            'healthyThreshold': context.properties['autohealingHealthyThreshold'],
            'unhealthyThreshold': context.properties['autohealingUnhealthyThreshold'],
            'httpsHealthCheck': {
                'port': context.properties['autohealingHttpsHealthCheck'],
            }
        }
    }, {
        'name': context.env['deployment'] + '-mig',
        'type': 'compute.v1.instanceGroupManager',
        'properties': {
            'baseInstanceName': context.env['deployment'] + '-instance',
            'instanceTemplate': '$(ref.' + ''.join([context.env['deployment'], '-fgt-template']) + '.selfLink)',
            'targetPools': ['$(ref.' + ''.join([context.env['deployment'], '-elb-target']) + '.selfLink)'],
            'targetSize': context.properties['targetSize'],
            'zone': context.properties['zone'],
            'autoHealingPolicies': [
                {
                    'healthCheck': '$(ref.' + ''.join([context.env['deployment'], '-hc-mig']) + '.selfLink)',
                    'initialDelaySec': context.properties['initialDelaySec'],
                }
            ]
        }
    }, {
        'name': 'fgt-template',
        'type': '../../templates/aa-fgt-instance-template.py',
        'properties': {
            'canIpForward': context.properties['canIpForward'],
            'image': context.properties['image'],
            'imageProject': context.properties['imageProject'],
            'machineType': context.properties['machineType'],
            'zone': context.properties['zone'],
            'metadata-from-file': {
                'user-data': 'fgt-bootstrap'
            },
            'serviceAccounts': [{
                'email': context.properties['serviceAccountEmail'],
                'scopes': context.properties['scopes']
            }],
            'vpcs': [{
                'vpc': 'public-vpc',
                'subnet': 'public-vpc-subnet',
                'accessConfigs': []
            }, {
                'vpc': 'private-vpc',
                'subnet': 'private-vpc-subnet',
                'accessConfigs': []
            }]
        }
    }, {
        'name': context.env['deployment'] + '-cloud-router',
        'type': 'compute.v1.routers',
        'properties': {
            'network': ''.join(['projects/', context.env['project'], '/global/networks/', context.env['deployment'], '-public-vpc']),
            'region': context.properties['region'],
            'nats': [{
                'name': context.env['deployment'] + '-nat-gw',
                'sourceSubnetworkIpRangesToNat': 'ALL_SUBNETWORKS_ALL_IP_RANGES',
                'natIpAllocateOption': 'AUTO_ONLY'
            }]
        },
        'metadata': {
            'dependsOn': [''.join([context.env['deployment'], '-public-vpc'])]
        }
    }, {
        'name': context.env['deployment'] + '-hc-ilb',
        'type': 'compute.v1.healthCheck',
        'properties': {
            'type': 'TCP',
            'tcpHealthCheck': {
                'port': context.properties['ilbHcPort']
            },
        }
    }, {
        'name': context.env['deployment'] + '-ilb',
        'type': 'compute.v1.regionBackendService',
        'properties': {
            'region': context.properties['region'],
            'network': ''.join(['projects/', context.env['project'], '/global/networks/', context.env['deployment'], '-private-vpc']),
            'healthChecks': ['$(ref.' + ''.join([context.env['deployment'], '-hc-ilb']) + '.selfLink)'],
            'protocol': 'TCP',
            'loadBalancingScheme': 'INTERNAL',
        },
        'metadata': {
            'dependsOn': [''.join([context.env['deployment'], '-private-vpc'])]
        }
    }, {
        'name': context.env['deployment'] + '-ilb-fr',
        'type': 'compute.v1.forwardingRule',
        'properties': {
            'allPorts': True,
            'network': ''.join(['projects/', context.env['project'], '/global/networks/', context.env['deployment'], '-private-vpc']),
            'subnetwork': '$(ref.' + context.env['deployment'] + '-private-vpc-subnet.selfLink)',
            'region': context.properties['region'],
            'backendService': '$(ref.' + ''.join([context.env['deployment'], '-ilb']) + '.selfLink)',
            'loadBalancingScheme': 'INTERNAL'
        }
    }, {
        'name': context.env['deployment'] + '-elb-hc',
        'type': 'compute.v1.httpHealthCheck',
        'properties': {
            'checkIntervalSec': context.properties['elbCheckIntervalSec'],
            'timeoutSec': context.properties['elbTimeoutSec'],
            'unhealthyThreshold': context.properties['elbUnhealthyThreshold'],
            'port': context.properties['elbHcPort']
        }
    }, {
        'name': context.env['deployment'] + '-elb-target',
        'type': 'compute.v1.targetPool',
        'properties': {
            'region': context.properties['region'],
            'healthChecks': ['$(ref.' + ''.join([context.env['deployment'], '-elb-hc']) + '.selfLink)']
        }
    }, {
        'name': context.env['deployment'] + '-elb-fr',
        'type': 'compute.v1.forwardingRule',
        'properties': {
            'region': context.properties['region'],
            'loadBalancingScheme': 'EXTERNAL',
            'target': '$(ref.' + context.env['deployment'] + '-elb-target'+'.selfLink)'
        }
    }, {
        'name': 'bastion-instance',
        'type': '../../templates/nginx-instance-template.py',
        'properties': {
            'image': context.properties['windowsImage'],
            'machineType': context.properties['windowsMachineType'],
            'metadata-from-file': {},
            'zone': context.properties['zone'],
            'vpcs': [{'vpc': 'public-vpc',
                      'subnet': 'public-vpc-subnet',
                      'accessConfigs': [{
                          'natIP': '$(ref.' + context.env['deployment'] + '-static-ip.address)',
                          'name': 'External NAT',
                          'type': 'ONE_TO_ONE_NAT'
                      }]}
                     ]
        }
    }]
    return {'resources': resources}
