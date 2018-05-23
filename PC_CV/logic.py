
import io

from PIL import Image

from .vision.google_api import Google_API


def my_logic(imgbytes, tags_raw, faces_raw):
    """Give an image, some annotations and return what you need in the template
    """
    imgpil = Image.open(io.BytesIO(imgbytes))  # Pillow library

    #TODO: your logic!
    topic = tags_raw[0].description if tags_raw else "nothing"
    topic = faces_raw if faces_raw else "nothing"
    imgpil = imgpil.convert("L")  # image to grayscale

    # Pillow image to PNG bytearray
    imgbuffer = io.BytesIO()
    imgpil.save(imgbuffer, 'PNG')
    imgpng = imgbuffer.getvalue()
    return (imgpng, topic)
