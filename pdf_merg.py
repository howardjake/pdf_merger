import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(list):
    merger = PyPDF2.PdfMerger()
    for pdf in list:
        merger.append(pdf)
    merger.write('super.pdf')
pdf_combiner(inputs)