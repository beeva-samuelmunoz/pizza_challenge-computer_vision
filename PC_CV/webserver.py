
import base64

import bottle
from bottle import route, run, request, post, view


from . import config
from . import logic

from .vision.google_api import Google_API
from .vision.azure_api import Azure_API
import uuid


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
    imgbytes = base64.b64decode(imgb64)

    # Debug, write to disk
    filename = '/tmp/{}.png'.format(uuid.uuid1())
    print(filename)
    with open(filename, 'wb') as f:
        f.write(imgbytes)

    #TODO: your logic (modularize it to easy debug)
    #tags_raw = g_client.annotate(imgbytes)
    faces_raw = az_client.face_detect(filename)
    img_png, topic = logic.my_logic(imgbytes, None, faces_raw=faces_raw)
    #img_png, topic = logic.my_logic(imgbytes, tags_raw)

    return {
        "image_grayscale": b"data:image/png;base64,"+base64.b64encode(img_png),
        "topic": topic
    }



if __name__=="__main__":
    #TODO: create clients you will need
    g_client = Google_API(config.GOOGLE_KEY)
    az_client = Azure_API(config.AZURE_KEY)

    # Webserver
    bottle.TEMPLATE_PATH = [config.BOTTLE_PATH_VIEWS]
    bottle.BaseRequest.MEMFILE_MAX = config.BOTTLE_MAX_BYTES_BODY
    run(host=config.BOTTLE_HOST, port=config.BOTTLE_PORT)
