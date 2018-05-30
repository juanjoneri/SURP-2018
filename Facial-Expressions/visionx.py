import io
from google.cloud import vision
from google.cloud.vision import types

path_to_image = './guido.jpg'

def detect_face(face_file, max_results=4):
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations


with io.open(path_to_image, 'rb') as image_file:
    response = detect_face(image_file)

print(response)
