import pyandoc

def docx_to_pdf(docx_file, pdf_file):
  pypandoc.convert_file(docx_file, 'pdf', outputfile=pdf_file)

# Usage
docx_to_pdf('/Users/aliamahama-rodriguez/Documents/input_file.docx', '/Users/aliamahama-rodriguez/Downloads/output_file.pdf')
