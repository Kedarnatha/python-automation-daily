# 📄 PDF Split Automation using Python

## 🚀 Project Overview

This project automatically splits a PDF document into individual pages using Python.

Each page from the input PDF is saved as a separate PDF file inside the output folder.

---

## 🧠 Technologies Used

- Python
- PyPDF2

---

## 📂 Project Structure

Day05_PDF_Split_Automation/

├── split_pdf.py  
├── pdfs/  
│   └── sample.pdf  
├── output/  
└── README.md  

---

## ⚙️ Features

- Split a PDF into individual pages
- Save each page as a separate PDF file
- Simple and easy-to-use automation script

---

## ▶️ How to Run

### 1. Install Required Library

```bash
pip install PyPDF2
```

### 2. Add Input PDF

Place the PDF file inside the `pdfs` folder.

Example:

```text
pdfs/
└── sample.pdf
```

### 3. Run the Script

```bash
python split_pdf.py
```

---

## 💻 Code

```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("pdfs/sample.pdf")

for page_num in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[page_num])

    output_file = f"output/page_{page_num + 1}.pdf"

    with open(output_file, "wb") as f:
        writer.write(f)

print("PDF split completed ✅")
```

---

## ✅ Example Output

Input:

```text
sample.pdf (5 pages)
```

Output:

```text
output/
├── page_1.pdf
├── page_2.pdf
├── page_3.pdf
├── page_4.pdf
└── page_5.pdf
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Working with PDF files in Python
- Reading PDF documents
- Writing PDF files
- File automation concepts
- Using the PyPDF2 library

---

## 🔥 Future Improvements

- Split specific page ranges
- Extract text from PDFs
- Merge multiple PDFs
- Password-protect PDFs
- Build a GUI version

---

## 👨‍💻 Author

Kedar