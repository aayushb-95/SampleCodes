import csv
import os

directory = '/home/aayush/Downloads/Master_Data_Trailer_V10_non_rotated_backup/images_combine/'
output_file = 'filename_csv.csv'

# Get all file names in the directory
filenames = []
for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        filenames.append(filename)

# Write filenames to CSV file
with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['filename'])  # Write column name
    for filename in filenames:
        writer.writerow([filename])

print("File names written to", output_file)
