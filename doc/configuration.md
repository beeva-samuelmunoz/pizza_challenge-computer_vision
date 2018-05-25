# Pizza Challenge - Computer Vision

## Configuration
All the configuration is held in the file `PC_CV/config_local.py`. Do not commit this file as it will contain sensitive information.

Start the virtual environment (just for this time).

```bash
source venv/bin/activate
```

### Credentials for Google Cloud Vision API

#### How to install gcloud
```bash
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

Generate an authentication token:
```bash
gcloud auth application-default login
```
Print the token
```bash
gcloud auth  application-default print-access-token
```
Copy the token into the variable `GOOGLE_KEY`in `config_local.py`.


### Credentials for Azure Cognitive Face API
Generate API key via https://azure.microsoft.com/es-es/try/cognitive-services/?api=face-api
Copy the key into the variable `AZURE_KEY` in `config_local.py`

### Credentials for Amazon Rekognition
Ask for your temporary access key and secret key. 
Copy into the variables AWS_KEY and AWS_KEY_ID

### Run!
Now you can [run](running.md) successfully your web demo
