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

```bash
#!/bin/bash
# Check if input and output files are provided
# This line is a conditional statement in a bash script that checks if the number of command-line arguments passed to the script is not equal to 2.
# 2=input+output (1+1) statements; otherwise, system prints a usage message and exits with a status code of '1', indicating that there was an error.
if [



#!/bin/bash

# Check if input and output files are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 input.pdf output.docx"
    exit 1
fi

input_file=$1
output_file=$2

# Convert PDF to plain text using pdftotext
pdftotext "$input_file" temp.txt

# Convert plain text to Word using pandoc
pandoc temp.txt -o "$output_file"

# Cleanup temporary file
rm temp.txt

echo "Conversion complete. Word file saved as $output_file."
