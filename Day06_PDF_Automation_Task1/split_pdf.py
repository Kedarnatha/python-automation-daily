from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("pdfs/sample.pdf")

for page_num in range(len(reader.pages)):
    writer = PdfWriter()
    writer.add_page(reader.pages[page_num])

    output_file = f"output/page_{page_num + 1}.pdf"

    with open(output_file, "wb") as f:
        writer.write(f)

print("PDF split completed ✅")