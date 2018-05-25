import io
import os

from PIL import Image, ImageFilter

from .vision.google_api import Google_API
from .vision.azure_api import Azure_API
import uuid


def crop_and_transpose_face(img, rect):
    left = rect['left']
    top = rect['top']
    width = rect['width']
    height = rect['height']
    box = (left, top, left +width, top + height)
    ic = img.crop(box)
    ic = ic.transpose(Image.ROTATE_180)
    img.paste(ic, box)
    return img

def my_logic(imgbytes, g_client, az_client, aws_client):
    """Give an image, some annotations and return what you need in the template
    """

    imgpil = Image.open(io.BytesIO(imgbytes))  # Pillow library

    #TODO: your logic (modularize it to easy debug)

    # Detect faces
    img_path = '/tmp/{}.png'.format(uuid.uuid1())
    imgpil.save(img_path,'PNG')  # TODO: ñapa
    faces_raw = az_client.face_detect(img_path)
    os.remove(img_path)  # No longer needed

    if (faces_raw and faces_raw[0]['faceRectangle']):
        topic = "face"
        rect = faces_raw[0]['faceRectangle']
        imgpil = crop_and_transpose_face(imgpil, rect)
        #ic = ic.filter(ImageFilter.BLUR)
    else:  # If no faces...what can I see?
        tags_raw = g_client.annotate(imgbytes)
        topic = tags_raw[0].description if tags_raw else "nothing"
        imgpil = imgpil.convert("L")  # image to grayscale
    # What can I read?
    ret = aws_client.detect_text(imgbytes)['TextDetections']
    ocr_lines = [
        element['DetectedText']
        for element in
        ret
        if element['Type']=='LINE'
    ]


    # Pillow image to PNG bytearray
    imgbuffer = io.BytesIO()
    imgpil.save(imgbuffer, 'PNG')
    imgpng = imgbuffer.getvalue()
    return (imgpng, topic, ocr_lines)
