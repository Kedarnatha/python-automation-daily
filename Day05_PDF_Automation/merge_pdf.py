from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

pdf_folder = "pdfs"

files = os.listdir(pdf_folder)

print("Files found:", files)

for file in files:
    if file.lower().endswith(".pdf"):
        path = os.path.join(pdf_folder, file)
        print("Adding:", path)
        merger.append(path)

# create output folder if not exists
os.makedirs("output", exist_ok=True)

merger.write("output/merged.pdf")
merger.close()

print("PDFs merged successfully ✅")