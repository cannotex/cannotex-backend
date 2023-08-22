import io
import parser
from io import BytesIO

#HERE COMES THE TESSERACT

### I want here it to import the Tesseract cloud client library, whatever it is

from tesseract.cloud import vision
from tesseract.cloud.vision import types
# Instantiates a client
from tesseract.protobuf.json_format import MessageToDict

def get_text(image_path):
    try:
        client = vision.ImageAnnotatorClient()
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        # Performs text detection on the image file
        response = client.document_text_detection(image=image)
        return MessageToDict(response, preserving_proto_field_name=True)['text_annotations']
    except IOError:
        return None

def get_text_from_pil_object(image_object):
    try:
        client = vision.ImageAnnotatorClient()
        buffered = BytesIO()
        image_object.save(buffered, format="JPEG")
        content = buffered.getvalue()
        image = types.Image(content=content)
        # Performs text detection on the image file
        response = client.document_text_detection(image=image)
        return MessageToDict(response, preserving_proto_field_name=True)['text_annotations']
    except IOError:
        return None
