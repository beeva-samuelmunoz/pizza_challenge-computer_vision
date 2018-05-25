
import base64
import uuid

import bottle
from bottle import route, run, request, post, view

from . import config
from . import logic
# Vision clients
from .vision.google_api import Google_API
from .vision.azure_api import Azure_API
from .vision.aws_api import AWS_API


@route('/')
@view('capture')
def capture():
    return None


@route('/image', method='POST')
@view('result')
def result():
    imgb64 = request.forms.get("image")
    if imgb64.startswith('data:'):  # data:image/png;base64,iVB
        imgb64 = imgb64[imgb64.find(',')+1 : ]
    imgbytes = base64.b64decode(imgb64)  # Image is bytes b''

    img_png, topic, ocr_lines = logic.my_logic(imgbytes, g_client, az_client, aws_client)

    return {
        "image": b"data:image/png;base64,"+base64.b64encode(img_png),
        "topic": topic,
        "ocr_lines": ocr_lines
    }



if __name__=="__main__":
    #Clients you will need
    g_client = Google_API(config.GOOGLE_KEY)
    az_client = Azure_API(config.AZURE_KEY, config.AZURE_URL)
    aws_client = AWS_API(key_id=config.AWS_KEY_ID, key=config.AWS_KEY)

    # Webserver
    bottle.TEMPLATE_PATH = [config.BOTTLE_PATH_VIEWS]
    bottle.BaseRequest.MEMFILE_MAX = config.BOTTLE_MAX_BYTES_BODY
    run(host=config.BOTTLE_HOST, port=config.BOTTLE_PORT)
