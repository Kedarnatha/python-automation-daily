# 📄 PDF Merge Automation using Python

## 🚀 Project Overview
This project automatically merges multiple PDF files into a single PDF using Python.

The script scans all PDF files inside the `pdfs/` folder and combines them into one merged PDF.

---

## 🧠 Technologies Used
- Python
- PyPDF2

---

## 📂 Project Structure

Day05_PDF_Automation/
│
├── merge_pdfs.py
├── pdfs/
├── output/
└── README.md

---

## ▶️ How to Run

### 1️⃣ Install Required Library

```bash
pip install PyPDF2
```

### 2️⃣ Add PDF Files

Place all PDF files inside the `pdfs/` folder.

Example:

```text
pdfs/
│
├── file1.pdf
├── file2.pdf
└── file3.pdf
```

### 3️⃣ Run the Script

```bash
python merge_pdfs.py
```

---

## ✅ Output

Merged PDF will be generated inside the `output/` folder.

Example:

```text
output/merged.pdf
```

---

## 💻 Example Code

```python
from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

pdf_folder = "pdfs"

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        merger.append(f"{pdf_folder}/{file}")

merger.write("output/merged.pdf")
merger.close()

print("PDFs merged successfully ✅")
```

---

## 🔥 Future Improvements

- Split PDFs
- Extract text from PDFs
- Password-protect PDFs
- GUI version
- AI document summarizer

---

## 📌 Author

Kedar