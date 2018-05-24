
import os


BOTTLE_HOST = '0.0.0.0'
BOTTLE_PORT = 8080
BOTTLE_PATH_VIEWS = os.path.dirname(__file__)+"/views"  # path for templates
BOTTLE_MAX_BYTES_BODY = 10*(2**20)  # 10MB max file


# API secrets not in commited files! -> config_local.py
GOOGLE_KEY = "replace with key"
AZURE_KEY = "replace with key"



try:
    from .config_local import *
except:
    pass
