import cognitive_face as CF


class Azure_API:

    def __init__(self, access_token):

        BASE_URL = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0'
        CF.BaseUrl.set(BASE_URL)
        CF.Key.set(access_token)
        
        self.client=CF
        self.client_face=CF.face


    def face_detect(self, url=None):
        """Annotate an image from 2 sources, choose one.
        imgbytes: image bytes
        url: public url of the image
        """
        ### TODO: put your logic here. Example:

        result = None

        try:
            result = self.client.face.detect(url, attributes='gender,age')
        except Exception as e:
            print(e)
        return(result)


## Test faces

if __name__=="__main__":
    import io
    import os
    import sys
    from PC_CV.config import AZURE_KEY

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
        client = Azure_API(access_token=AZURE_KEY)
        faces = client.face_detect(img_path)
        print(faces)
    except Exception as e:
        print(e)
