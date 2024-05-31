# Document-Conversions
Convert files to different formats.

## Python Script

We use the `pdf2docx` library to convert PDF files to Word files in Python. First, install the library using pip command:
```python
pip install pdf2docx
```
Then, you can use the following Python script:
```python
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
```

Replace `'input.pdf` with the path to your PDF file and `'output.docx'` with the desired path for the output Word file.

Alternatively, you can utilize the `pdftotext` and `pandoc` command-line tools to convert PDF files to Word files. First, ensure you have both tools installed. On Ubuntu, you can install them using:
````**********
