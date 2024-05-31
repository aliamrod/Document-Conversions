from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def txt_to_pdf(txt_file, pdf_file):
  with open(txt_file, 'r') as file:
    text = file.read()
  c = canvas.Canvas(pdf_file, pagesize=letter)
  c.drawString(100, 750, text)
  c.save()

# Usage
txt_to_pdf('/Users/aliamahama-rodriguez/Documents/input_file.txt', '/Users/aliamahama-rodriguez/Downloads/output_file.pdf')
