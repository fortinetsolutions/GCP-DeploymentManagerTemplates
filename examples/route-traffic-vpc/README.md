# Route Traffic through FortiGate to Web Server within VPC (same region)

This example creates a Fortigate Instance with BYOL, Ubuntu Instance (with nginx installed), an External IP, Compute Forwarding Rules, Compute Target Instance and bootstrap Fortigate with Static Route, Virtual IP, Firewall Policy which routes traffic through FortiGate to Ubuntu Instance (nginx) .

This is a Google Cloud Deployment Manager configuration file that creates a Fortigate Instance with BYOL, Ubuntu Instance (with nginx installed), an External IP, Compute Forwarding Rules, Compute Target Instance and bootstrap Fortigate with Static Route, Virtual IP, Firewall Policy which routes traffic through FortiGate to Ubuntu Instance (nginx) along with bootstrapping the License file and password.

To use it, do a git clone of this repo and cd into the folder. Have gcloud installed and select/create a approrpiate <PROJECT_ID>

Provide the <FGT_IMAGE> and upload <LICENSE_FILE> in the license folder.

Then run

###### Deploy the resources

```
gcloud deployment-manager deployments create deployment-route-traffic-vpc --config route-traffic-vpc.yaml

```

If the deployment is successful, you receive a message similar to the following example:

```
NAME                                               TYPE                        STATE      ERRORS  INTENT
deployment-route-traffic-vpc-fgt-instance          compute.v1.instance         COMPLETED  []
deployment-route-traffic-vpc-firewall-egress       compute.v1.firewall         COMPLETED  []
deployment-route-traffic-vpc-firewall-ingress      compute.v1.firewall         COMPLETED  []
deployment-route-traffic-vpc-forwarding-rules-tcp  compute.v1.forwardingRules  COMPLETED  []
deployment-route-traffic-vpc-forwarding-rules-udp  compute.v1.forwardingRules  COMPLETED  []
deployment-route-traffic-vpc-nginx-instance        compute.v1.instance         COMPLETED  []
deployment-route-traffic-vpc-static-ip             compute.v1.addresses        COMPLETED  []
deployment-route-traffic-vpc-subnet                compute.v1.subnetwork       COMPLETED  []
deployment-route-traffic-vpc-target-instance       compute.v1.targetInstances  COMPLETED  []
deployment-route-traffic-vpc-vpc                   compute.v1.network          COMPLETED  []
OUTPUTS              VALUE
External IP Address  <EXTERNAL_IP_ADDRESS>
FortiGate IP         <FGT_MGMT_IP>
Username             admin
password             <FGT_PASSWORD>
```

###### Check on your new deployment
To check the status of the deployment, run the following command:

```
gcloud deployment-manager deployments describe deployment-single-fgt
```

For a quick introduction to Deployment Manager, see the Quickstart tutorial.
