import pdfplumber

pdf = pdfplumber.open("main.pdf")
text = len(pdf.chars)
print(text)
