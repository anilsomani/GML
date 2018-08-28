import io
import sys
from google.cloud import vision

vision_client = vision.Client();

if len(sys.argv) < 2: 
    print("Filename missing") 
    sys.exit();

file_name = sys.argv[1];
print("Scanning file " + file_name)

with io.open(file_name, 'rb') as image_file:
    content = image_file.read();
    image = vision_client.image(content=content)

print(image.detect_full_text().text)

labels = image.detect_labels()

for label in labels:
    print(label.description) 
