from google.cloud.vision import ImageAnnotatorClient, types
from google.oauth2.credentials import Credentials


class Google_API:

    def __init__(self, access_token):
        self.client = ImageAnnotatorClient(
            credentials=Credentials(access_token)
        )


    def annotate(self, imgbytes=None, url=None):
        """Annotate an image from 2 sources, choose one.
        imgbytes: image bytes
        url: public url of the image
        """
        image = types.Image(content=imgbytes, source=url)
        # Functions available: https://google-cloud-python.readthedocs.io/en/latest/vision/gapic/v1/api.html

        ### TODO: put your logic here. Example:
        response = self.client.label_detection(image=image)  # Label detection

        return(response.label_annotations)


# Test annotations
if __name__=="__main__":
    import io
    import os
    import sys
    from PC_CV.config import GOOGLE_KEY

    if len(sys.argv) != 2:  # Number of arguments correct
        print("Usage: {} <path of an image>".format(sys.argv[0]))
        exit(0)
    img_path = sys.argv[1]
    if not os.path.isfile(img_path):  # File exists
        print("ERROR: cannot find {}".format(img_path))
        exit(0)

    try:
        with io.open(img_path, 'rb') as image_file:
            content = image_file.read()
        client = Google_API(access_token=GOOGLE_KEY)
        labels = client.annotate(content)
        print(labels)
    except Exception as e:
        print(e)
