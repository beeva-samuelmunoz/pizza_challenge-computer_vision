import io
import os

from PIL import Image

from .vision.google_api import Google_API
from .vision.azure_api import Azure_API
import uuid


def process_face(faces_raw):
    topic = "face"

    return topic

def my_logic(imgbytes, az_face_client, g_annotation_client):
    """Give an image, some annotations and return what you need in the template
    """

    # Debug, write to disk
    filename = '/tmp/{}.png'.format(uuid.uuid1())
    print(filename)
    with open(filename, 'wb') as f:
        f.write(imgbytes)

    #TODO: your logic (modularize it to easy debug)

    faces_raw = az_face_client.face_detect(filename)

    if (faces_raw and faces_raw[0]['faceRectangle']):
        topic = process_face(faces_raw)
    else:
        tags_raw = g_annotation_client.annotate(imgbytes)
        topic = tags_raw[0].description if tags_raw else "nothing"

    imgpil = Image.open(io.BytesIO(imgbytes))  # Pillow library

    #TODO: your logic!
    imgpil = imgpil.convert("L")  # image to grayscale

    # Pillow image to PNG bytearray
    imgbuffer = io.BytesIO()
    imgpil.save(imgbuffer, 'PNG')
    imgpng = imgbuffer.getvalue()

    os.remove(filename)
    return (imgpng, topic)
