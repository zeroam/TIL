"""csv_reader_obj.py
csv 모듈의 reader object 활용
"""
import csv

example_file = open("example.csv")
example_reader = csv.reader(example_file)
example_data = list(example_reader)
print(example_data)
print(example_data[0][0])  # 1행 1열 데이터
print(example_data[0][1])  # 1행 2열 데이터

# reader object으로 for문 돌기
example_file = open("example.csv")
example_reader = csv.reader(example_file)
for row in example_reader:
    print(f"Row # {example_reader.line_num} {row}")
