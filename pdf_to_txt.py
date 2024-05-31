import pdfplumber

def pdf_to_text(pdf_file, txt_file):
  with pdfplumber.open(pdf_file) as pdf:
    text = ''
    for page in pdf.pages:
      text += page.extract_text()
    with open(txt_file, 'w') as file:
      file.write(text)

# Usage
pdf_to_txt('/Users/aliamahama-rodriguez/Downloads/input_file.pdf', 'Users/aliamahama-rodriguez/Documents/output_file.txt')
