# HA Active - Passive

This example creates a HA Active-Passive configuration.

## Instances included in this Example

1. 4 VPC Networks
    - Public/Internal
    - Private/External
    - Sync
    - Management
1. Subnets for each VPC Network
    - Public/Internal
    - Private/External
    - Sync
    - Management
1. Firewalls
    - Creates 'INGRESS' and 'EGRESS' rules allowgin all protocols.
1. Route
    - Creates a route which has 'Next Hop IP' defined.
1. External/Static IP
1. 2 Instances
    - Active
        - Deploys License
        - Updates Password
        - Updates Interfaces
        - Configures HA
        - Configures GCP SDN Connector
    - Passive
        - Deploys License
        - Updates Password
        - Updates Interfaces
        - Configures HA
        - Configures GCP SDN Connector


To use it, do a git clone of this repo and cd into the ha-active-passive folder under examples.

Make sure you have gcloud installed and configured.

Provide the <FORTIGATE_VM_IMAGE>, upload <LICENSE_FILE> license files in the license folder and provide the <PATH_TO_LICENSE_FILE> (FGT LICENSE PATH) path in ha-active-passive.yaml file.

NOTE: The example provided is for the CIDR 172.18.0.0/24 - 172.18.3.0/24, but if you have to update the CIDR Range, please udpate it in ha-active-passive.yaml file for Subnets, and appropriately update the active and passive scripts where the IP Address defined for Interfaces and HA.

Then run

###### Deploy the resources

```
gcloud deployment-manager deployments create deployment-ha --config ha-active-passive.yaml

```

If the deployment is successful, you receive a message similar to the following example:

```
NAME                                        TYPE                   STATE      ERRORS  INTENT
deployment-ha-fgt-active-instance           compute.v1.instance    COMPLETED  []
deployment-ha-fgt-passive-instance          compute.v1.instance    COMPLETED  []
deployment-ha-ha-vpc                        compute.v1.network     COMPLETED  []
deployment-ha-ha-vpc-firewall-egress        compute.v1.firewall    COMPLETED  []
deployment-ha-ha-vpc-firewall-ingress       compute.v1.firewall    COMPLETED  []
deployment-ha-ha-vpc-subnet                 compute.v1.subnetwork  COMPLETED  []
deployment-ha-log-disk                      compute.v1.disk        COMPLETED  []
deployment-ha-mgmt-vpc                      compute.v1.network     COMPLETED  []
deployment-ha-mgmt-vpc-firewall-egress      compute.v1.firewall    COMPLETED  []
deployment-ha-mgmt-vpc-firewall-ingress     compute.v1.firewall    COMPLETED  []
deployment-ha-mgmt-vpc-subnet               compute.v1.subnetwork  COMPLETED  []
deployment-ha-private-vpc                   compute.v1.network     COMPLETED  []
deployment-ha-private-vpc-firewall-egress   compute.v1.firewall    COMPLETED  []
deployment-ha-private-vpc-firewall-ingress  compute.v1.firewall    COMPLETED  []
deployment-ha-private-vpc-subnet            compute.v1.subnetwork  COMPLETED  []
deployment-ha-public-vpc                    compute.v1.network     COMPLETED  []
deployment-ha-public-vpc-firewall-egress    compute.v1.firewall    COMPLETED  []
deployment-ha-public-vpc-firewall-ingress   compute.v1.firewall    COMPLETED  []
deployment-ha-public-vpc-subnet             compute.v1.subnetwork  COMPLETED  []
deployment-ha-route                         compute.v1.routes      COMPLETED  []
deployment-ha-static-ip                     compute.v1.addresses   COMPLETED  []
OUTPUTS               VALUE
Cluster IP Address    <CLUSTER_IP_ADDRESS>
Active FortiGate IP   <ACTIVE_FGT_IP_ADDRESS>
Passive FortiGate IP  <PASSIVE_FGT_IP_ADDRESS>
Username              admin
password              <FGT_PASSWORD>

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
