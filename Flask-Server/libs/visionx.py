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

def detect_joy(uri):
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri
    response = client.face_detection(image=image)
    confidence = {
        'joy': response.face_annotations[0].joy_likelihood,
        'anger': response.face_annotations[0].anger_likelihood,
        'surprise': response.face_annotations[0].surprise_likelihood,
        'sorrow': response.face_annotations[0].sorrow_likelihood
    }
    return confidence
    

def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    client = vision.ImageAnnotatorClient()
    image = types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations

    return labels


if __name__ == '__main__':
    labels = detect_labels_uri('https://media.mnn.com/assets/images/2016/10/joy.jpg.653x0_q80_crop-smart.jpg')
    for label in labels:
        print(label.description)