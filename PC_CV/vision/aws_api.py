import boto3

"""
For a complete list of AWS Rekognition features, visit:
http://boto3.readthedocs.io/en/latest/reference/services/rekognition.html
"""

class AWS_API:

    def __init__(self, key_id, key):
        self.client = boto3.client('rekognition')
        client = boto3.client(
            's3',
            # Hard coded strings as credentials, not recommended.
            aws_access_key_id=key_id,
            aws_secret_access_key=key
        )


    def detect_text(self, imgbytes):
        """Annotate an image from 2 sources, choose one.
        imgbytes: image bytes
        url: public url of the image
        """
        self.client.detect_text(Image={'Bytes': imgbytes})


        image = types.Image(content=imgbytes, source=url)
        # Functions available:

        ### TODO: put your logic here. Example:
        response = self.client.label_detection(image=image)  # Label detection

        return(response.label_annotations)


# Test annotations
if __name__=="__main__":
    import io
    import os
    import sys
    from PC_CV.config import AWS_KEY, AWS_KEY_ID

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
        client = AWS_API(key_id=AWS_KEY_ID, key=AWS_KEY)
        labels = client.detect_text(content)
        print(labels)
    except Exception as e:
        print(e)
