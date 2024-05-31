import pypandoc

def md_to_html(md_file, html_file):
  pypandoc.convert_file(md_file, 'html', outputfile=html_file)

# Usage
md_to_html('./input_file.md', './output_file.html')
