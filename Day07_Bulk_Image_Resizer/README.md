# 🖼️ Bulk Image Resizer Automation

## 🚀 Project Overview

This Python automation project resizes multiple images at once and saves them to an output folder.

The script scans all images in the input directory, resizes them to a specified size, and stores the resized images in a separate output folder.

This helps automate repetitive image-processing tasks and saves time when working with large numbers of images.

---

## 🧠 Technologies Used

- Python
- Pillow (PIL)
- os module

---

## 📂 Project Structure

Day06_Image_Resizer/

├── resize_images.py

├── images/

├── output/

└── README.md

---

## ✨ Features

- Resize multiple images automatically
- Supports JPG, JPEG, and PNG formats
- Saves resized images to a separate folder
- Batch image processing
- Beginner-friendly Python automation project

---

## 📦 Installation

Install the required library:

```bash
pip install pillow
```

---

## ▶️ How to Run

### 1. Add Images

Place all images inside the `images` folder.

Example:

```text
images/
├── photo1.jpg
├── photo2.png
└── photo3.jpeg
```

### 2. Run the Script

```bash
python resize_images.py
```

### 3. Check Output

The resized images will be available in the `output` folder.

---

## 💻 Code

```python
from PIL import Image
import os

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(INPUT_FOLDER, file)

        img = Image.open(image_path)

        img = img.resize((800, 600))

        output_path = os.path.join(OUTPUT_FOLDER, file)

        img.save(output_path)

        print(f"Resized: {file}")

print("All images resized successfully ✅")
```

---

## 📊 Example

### Input

```text
photo1.jpg (4000x3000)
photo2.png (3000x2000)
```

### Output

```text
photo1.jpg (800x600)
photo2.png (800x600)
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Working with image files in Python
- Batch processing multiple files
- Using the Pillow library
- Automating repetitive tasks
- Managing files and folders with Python

---

## 🔥 Future Improvements

- Preserve aspect ratio automatically
- Rename resized images
- Convert images to PNG format
- Generate thumbnails
- Add GUI using Tkinter
- Build a web version using Django

---

## 👨‍💻 Author

Kedar
