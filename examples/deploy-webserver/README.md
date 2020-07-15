# Webserver deployment with nginx installed

This is a Google Cloud Deployment Manager configuration file that has Ubuntu image with nginx installed.

To use it, do a git clone of this repo and cd into the folder. Have gcloud installed and select/create a approrpiate <PROJECT_ID>

Then run

###### Deploy the resources

```
gcloud deployment-manager deployments create deployment-nginx-webserver --config nginx.yaml

```

If the deployment is successful, you receive a message similar to the following example:

```
NAME                                 TYPE                   STATE      ERRORS  INTENT
deployment-nginx-webserver-firewall  compute.v1.firewall    COMPLETED  []
deployment-nginx-webserver-instance  compute.v1.instance    COMPLETED  []
deployment-nginx-webserver-subnet    compute.v1.subnetwork  COMPLETED  []
deployment-nginx-webserver-vpc       compute.v1.network     COMPLETED  []
OUTPUTS             VALUE
NGINX Webserver IP  <IP_ADDRESS>
```

###### Check on your new deployment
To check the status of the deployment, run the following command:

```
gcloud deployment-manager deployments describe deployment-nginx-webserver
```

For a quick introduction to Deployment Manager, see the Quickstart tutorial.
