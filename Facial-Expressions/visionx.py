import io
from google.cloud import vision

vision_client = vision.Client()
path_to_image = 'path'

with io.open(path_to_image, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(content=content)

labels = image.detect_labels()
for label in labels:
    print(label.description)