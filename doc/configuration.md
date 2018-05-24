# Pizza Challenge - Computer Vision

## Configuration
All the configuration is held in the file `PC_CV/config_local.py`. Do not commit this file as it will contain sensitive information.

Start the virtual environment (just for this time).

```bash
source venv/bin/activate
```

### Credentials for Google Cloud Vision API
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
Ask for your API key and copy into the variable `AZURE_KEY` in `config_local.py`

### Run!
Now you can [run](running.md) successfully your web demo
