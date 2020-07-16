"""csv_remove_header.py
removeCsvHeader 디렉터리에 있는
CSV 파일들의 헤더 없애고
header_removed 디렉터리에 생성
"""
import os
import csv

os.makedirs("header_removed", exist_ok=True)

# Loop through every file in the current working directory
dir_name = "removeCsvHeader"
for folder, sub_folder, file_names in os.walk(dir_name):
    for file_name in file_names:
        if not file_name.endswith(".csv"):
            continue

        print(f"Removing head from {file_name}")

        # Read the CSV file in (skipping first row)
        csv_rows = []
        csv_file_obj = open(os.path.join(folder, file_name))
        csv_reader = csv.reader(csv_file_obj)
        for row in csv_reader:
            if csv_reader.line_num == 1:
                continue  # skip first row
            csv_rows.append(row)
        csv_file_obj.close()

        # Write out the CSV file
        csv_file_obj = open(os.path.join("header_removed", file_name), "w", newline="")
        csv_writer = csv.writer(csv_file_obj)
        for row in csv_rows:
            csv_writer.writerow(row)
        csv_file_obj.close()
