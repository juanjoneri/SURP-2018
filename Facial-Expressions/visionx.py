import io
from google.cloud import vision
from google.cloud.vision import types

path_to_image = './joy.jpg'

def detect_face(face_file, max_results=4):
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels:

#with io.open(path_to_image, 'rb') as image_file:
#   labels = detect_face(image_file)

#for label in labels:
#    print(labels)

if __name__ == '__main__':
    detect_labels_uri('https://media.mnn.com/assets/images/2016/10/joy.jpg.653x0_q80_crop-smart.jpg')
