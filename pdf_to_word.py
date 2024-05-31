from pdf2docx import Converter

def convert_pdf_to_word(pdf_file, word_file):
  # Initialize Converter object
  cv = Converter(pdf_file)

  # Convert PDF to Word
  cv.convert(word_file, start=0, end=None) # Used to convert the PDF file to Word document; start=0 parameter -> starting page index for conversion; `end=None` -> ending page index 

  # Close Converter object
  cv.close()

# Usage
pdf_file = '/Users/aliamahama-rodriguez/Downloads/input_file.pdf'
word_file = '/Users/aliamahama-rodriguez/Documents/output_file.docx'
convert_pdf_to_word(pdf_file, word_file)
