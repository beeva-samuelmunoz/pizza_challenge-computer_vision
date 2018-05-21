
import base64

import bottle
from bottle import route, run, request, post, view



from . import config


@route('/')
@view('capture')
def capture():
    return None


@route('/image', method='POST')
@view('result')
def result():
    imageb64 = request.forms.get("image")
    if imageb64.startswith('data:'):  # data:image/png;base64,iVB
        imageb64 = imageb64[imageb64.find(',')+1 : ]
    img = base64.b64decode(imageb64)

    # Debug
    # with open('test.png', 'wb') as f:
        # f.write(img)

    return {
        "image": b"data:image/png;base64,"+base64.b64encode(img)
    }



if __name__=="__main__":
    bottle.TEMPLATE_PATH = [config.BOTTLE_PATH_VIEWS]
    bottle.BaseRequest.MEMFILE_MAX = config.BOTTLE_MAX_BYTES_BODY
    run(host=config.BOTTLE_HOST, port=config.BOTTLE_PORT)
