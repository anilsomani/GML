import io
  2 import sys
  3 from google.cloud import vision
  4 from google.cloud.vision import types
  5
  6 vision_client = vision.ImageAnnotatorClient();
  7
  8 if len(sys.argv) < 2:
  9     print("Filename missing")
 10     sys.exit();
 11
 12 file_name = sys.argv[1];
 13 print("Scanning file " + file_name)
 14
 15 with io.open(file_name, 'rb') as image_file:
 16     content = image_file.read();
 17     image = types.Image(content=content)
 18
 19 response = vision_client.label_detection(image=image)
 20 labels = response.label_annotations
 21
 22 for label in labels:
 23     print(label.description)
 24
 25 response = vision_client.document_text_detection(image=image)
 26 texts = response.text_annotations
 27
 28 for text in texts:
 29     print(text.description)
