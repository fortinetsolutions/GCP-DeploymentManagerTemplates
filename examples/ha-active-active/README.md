# HA Active-Active

This example creates a HA Active-Active configuration.

![Image of HA Active/Active](/examples/ha-active-active/ha-active-active.png)

## Instances included in this Configuration

1. 2 VPC Networks
    - Public/Internal
    - Private/External
1. Subnets for each VPC Network
    - Public
    - Private
1. Firewalls
    - Creates 'INGRESS' and 'EGRESS' rules allowing all protocols.
1. Managed Instance Group
    - Autohealing
1. Instance Template
    - Including Bootstrap of configuration for FortiGate.
        - Configures admin_port, static route, probe-response, firewall service custom, firewall policy.
        - Adds loopback, Virtual IPs.
1. 2 Instances
1. Cloud Router
1. Internal Load Balancer
1. Health Check(s)
1. External Load Balancer

## Connection to FortiGate Management GUI
- To connect to the FortiGate Management GUI, one has to RDP into the Bastion Host and install Firefox.
- Once done, enter the Internal IP (nic0) of the FortiGate with port 8443 (or whatever defined in terraform.tfvars for 'admin_port')

To use it, do a git clone of this repo and cd into the ha-active-active folder under examples.

Make sure you have gcloud installed and configured.

Provide the <FORTIGATE_IMAGE>, <FGT_IMAGE_PROJECT> and <SERVICE_ACCOUNT_EMAIL> path in ha-active-active.yaml file.

NOTE: The example provided is for the CIDR 172.14.0.0/24 - 172.14.1.0/24, but if you have to update the CIDR Range, please udpate it in ha-active-active.yaml file for Subnets, and appropriately update the fgt-bootstrap script where the IP Address are defined.

Then run

###### Deploy the resources

```
gcloud deployment-manager deployments create deployment-ha --config ha-active-active.yaml

```

If the deployment is successful, you receive a message similar to the following example:

```
NAME                                        TYPE                             STATE      ERRORS  INTENT
deployment-ha-bastion-instance              compute.v1.instance              COMPLETED  []
deployment-ha-cloud-router                  compute.v1.routers               COMPLETED  []
deployment-ha-elb-fr                        compute.v1.forwardingRule        COMPLETED  []
deployment-ha-elb-hc                        compute.v1.httpHealthCheck       COMPLETED  []
deployment-ha-elb-target                    compute.v1.targetPool            COMPLETED  []
deployment-ha-fgt-template                  compute.v1.instanceTemplate      COMPLETED  []
deployment-ha-hc-ilb                        compute.v1.healthCheck           COMPLETED  []
deployment-ha-hc-mig                        compute.v1.healthCheck           COMPLETED  []
deployment-ha-ilb                           compute.v1.regionBackendService  COMPLETED  []
deployment-ha-ilb-fr                        compute.v1.forwardingRule        COMPLETED  []
deployment-ha-mig                           compute.v1.instanceGroupManager  COMPLETED  []
deployment-ha-private-vpc                   compute.v1.network               COMPLETED  []
deployment-ha-private-vpc-firewall-egress   compute.v1.firewall              COMPLETED  []
deployment-ha-private-vpc-firewall-ingress  compute.v1.firewall              COMPLETED  []
deployment-ha-private-vpc-subnet            compute.v1.subnetwork            COMPLETED  []
deployment-ha-public-vpc                    compute.v1.network               COMPLETED  []
deployment-ha-public-vpc-firewall-egress    compute.v1.firewall              COMPLETED  []
deployment-ha-public-vpc-firewall-ingress   compute.v1.firewall              COMPLETED  []
deployment-ha-public-vpc-subnet             compute.v1.subnetwork            COMPLETED  []
deployment-ha-static-ip                     compute.v1.addresses             COMPLETED  []

OUTPUTS                     VALUE
Bastion Host IP Address     <BASTION_HOST_IP_ADDRESS>
FortiGate Username          admin
FortiGate Password          fortinet

```

###### Check on your new deployment
To check the status of the deployment, run the following command:

```
gcloud deployment-manager deployments describe deployment-ha
```

###### Delete deployment
To delete the deployment, run the following command:

```
gcloud deployment-manager deployments delete deployment-ha
```

For a quick introduction to Deployment Manager, see the Quickstart tutorial.
