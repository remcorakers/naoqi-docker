"""
Google Vision allows us to analyse picture contents using machine learning.
In this example, you can see the response to a picture of Laurens' face from 'images/laurens.jpg'.
The response is a classification of the picture, stating that Laurens is a girl. (Might need some improvement)

If you're using the Zora robot, you can capture shots using the function takePicture()
http://doc.aldebaran.com/2-1/naoqi/vision/alphotocapture.html

Otherwise you can use a different way to capture pictures.
"""

import io
import os
from google.cloud import vision
from google.cloud.vision import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "creds.json"

client = vision.ImageAnnotatorClient()
file_name = os.path.join(
    os.path.dirname(__file__),
    'Images/laurens.jpg')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)

labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description + " - " + str(label.score))
