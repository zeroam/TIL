"""csv_header_file.py
DictReader, DictWriter를 이용한
헤더 정보가 있는 csv 파일 읽고 쓰기
"""
import csv

# 헤더 정보 생성해서 파일 읽기
example_file = open("example.csv")
example_dict_reader = csv.DictReader(example_file, ["time", "name", "amount"])
for row in example_dict_reader:
    print(row["time"], row["name"], row["amount"])


# 헤더 정보를 포함한 파일 쓰기
output_file = open("output.csv", "w", newline="")
output_dict_writer = csv.DictWriter(output_file, ["Name", "Pet", "Phone"])
output_dict_writer.writeheader()  # 헤더 쓰기
output_dict_writer.writerow({"Name": "Alice", "Pet": "cat", "Phone": "555-1234"})
output_dict_writer.writerow({"Name": "Bob", "Phone": "555-9999"})
output_dict_writer.writerow({"Phone": "555-5555", "Name": "Carol", "Pet": "dog"})
output_file.close()


# 헤더 정보를 포함한 파일 읽기
example_file = open("output.csv")
example_dict_reader = csv.DictReader(example_file)
for row in example_dict_reader:
    print(row["Name"], row["Pet"], row["Phone"])
