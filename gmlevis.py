import io
import sys
from google.cloud import vision
from google.cloud.vision import types

vision_client = vision.ImageAnnotatorClient();

if len(sys.argv) < 2:
  print("Filename missing")
  sys.exit();

file_name = sys.argv[1];
print("Scanning file " + file_name)

with io.open(file_name, 'rb') as image_file:
  content = image_file.read();
  image = types.Image(content=content)

response = vision_client.label_detection(image=image)
labels = response.label_annotations

for label in labels:
  print(label.description)

response = vision_client.document_text_detection(image=image)
texts = response.text_annotations

for text in texts:
  print(text.description)
