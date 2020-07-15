# Contains examples for configurations.

Contains examples of Google Cloud Deployment Manager configuration file(s).

To use it, do a git clone of this repo and cd into the appropriate examples folder. 

Make sure you have gcloud installed and select/create a approrpiate <PROJECT_ID>

Provide the <FGT_IMAGE> and upload <LICENSE_FILE> in the license folder.

Then run

###### Deploy the resources

```
gcloud deployment-manager deployments create <DEPLOYMENT_NAME> --config <CONFIG_FILE>

```

For a quick introduction to Deployment Manager, see the Quickstart tutorial.

1. https://cloud.google.com/deployment-manager/docs
1. https://cloud.google.com/deployment-manager/docs/quickstart
