# Excel (.xlsx) to CSV (.csv)

import pandas as pd

def excel_to_csv(excel_file, csv_file):
  df = pd.read_excel(excel_file)
  df.to_csv(csv_file, index=False)

# Usage
excel_to_csv('./input_file.xlsx', './output_file.csv')
