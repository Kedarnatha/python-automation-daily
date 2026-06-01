from PIL import Image
import os

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER,exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    if file.lower().endswith((".jpg",".jpeg",".png")):

        image_path = os.path.join(INPUT_FOLDER,file)

        img = Image.open(image_path)

        img = img.resize((800,800))

        output_path = os.path.join(OUTPUT_FOLDER,file)

        img.save(output_path)

        print(f"Resized:{file}")
print("All images resized successfully")
