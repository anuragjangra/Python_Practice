from PyPDF2 import PdfWriter

merger = PdfWriter()
pdfs = []

n = int(input("Enter the number of pdfs you want to merge: "))
for i in range(0, n):
    pdf = input(f"Enter the name of the pdf {i+1} file: ")
    pdfs.append(pdf)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_pdf.pdf")
print("PDFs merged successfully into 'merged_pdf.pdf'")
merger.close()
