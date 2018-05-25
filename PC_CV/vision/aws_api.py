import boto3

"""
For a complete list of AWS Rekognition features, visit:
http://boto3.readthedocs.io/en/latest/reference/services/rekognition.html

JSON return format:
https://docs.aws.amazon.com/rekognition/latest/dg/text-detection.html
"""

class AWS_API:

    def __init__(self, key_id, key):
        self.client = boto3.client(
            'rekognition',
            # Hard coded strings as credentials, not recommended.
            aws_access_key_id=key_id,
            aws_secret_access_key=key
        )


    def detect_text(self, imgbytes):
        """Identify text in the image
        """
        response = self.client.detect_text(Image={'Bytes': imgbytes})
        return(response)


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
