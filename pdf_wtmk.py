import PyPDF2
import sys

template  = PyPDF2.PdfReader(open(sys.argv[1], 'rb'))
watermark = PyPDF2.PdfReader(open(sys.argv[2], 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('watermarked.pdf', 'wb') as file:
    output.write(file)