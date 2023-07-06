import csv
import re

input_file = 'input.csv'
output_file = 'output.csv'
pattern = r'^\./.*?/.*?/.*?/'

with open(input_file, 'r') as csv_file, open(output_file, 'w', newline='') as output_csv:
    reader = csv.DictReader(csv_file)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        filename = row['filename']
        modified_filename = re.sub(pattern, '', filename)
        row['filename'] = modified_filename
        writer.writerow(row)

print("File processing completed!")
