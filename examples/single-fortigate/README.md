# Single FortiGate deployment

This is a Google Cloud Deployment Manager configuration file that deploys a single FortiGate VM along with bootstrapping the License file and password.

To use it, do a git clone of this repo and cd into examples/single-fortigate/ folder. 

Make sure you have gcloud installed and configured.

Provide the <FORTIGATE_VM_IMAGE> in single-fortigate-template.py template and upload <LICENSE_FILE> in the license folder.

Run the below command

###### Deploy the resources

```
gcloud deployment-manager deployments create deployment-single-fgt --config fortigate-byol.yaml

```

Once the deployment is successful, you receive a message similar to the following example:

```
NAME                            TYPE                   STATE      ERRORS  INTENT
deployment-single-fgt-firewall  compute.v1.firewall    COMPLETED  []
deployment-single-fgt-instance  compute.v1.instance    COMPLETED  []
deployment-single-fgt-subnet    compute.v1.subnetwork  COMPLETED  []
deployment-single-fgt-vpc       compute.v1.network     COMPLETED  []
OUTPUTS       VALUE
FortiGate IP  <FGT_IP>
Username      admin
password      <FGT_PASSWORD>
```

###### Check on your new deployment

To check the status of the deployment, run the following command:

```
gcloud deployment-manager deployments describe deployment-single-fgt
```

To delete the deployment, run the following command:

```
gcloud deployment-manager deployments delete deployment-single-fgt
```

For a quick introduction to Deployment Manager, see the Quickstart tutorial.
