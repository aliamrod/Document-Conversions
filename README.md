# Document-Conversions
Convert files to different formats.

## Python Script

We use the `pdf2docx` library to convert PDF files to Word files in Python. First, install the library using pip command:
```python
pip install pdf2docx
```
Then, you can use the followoing Python script:
```python
from pdf2docx import Converter

def convert_pdf_to_word(pdf_file, word_file):
  # Initialize Converter object
  cv = Converter(pdf_file)

  # Convert PDF to Word
  cv.convert(word_file, start=0, end=None)
  

```

Replace `'input.pdf` with the path to your PDF file and `'output.docx'` with the desired path for the output Word file.

Alternatively, you can utilize the `pdftotext` and `pandoc` command-line tools to convert PDF files to Word files. First, ensure you have both tools installed. On Ubuntu, you can install them using:
```bash
sudo apt update
sudo apt install poppler-utils pandoc
```
