"""csv_writer_obj.py
csv 모듈의 write obj 활용
"""
import csv

# 윈도우 OS에서는 newline을 세팅해주지 않으면 2줄 개행이 됨
output_file = open("output.csv", "w", newline="")
output_writer = csv.writer(output_file)

output_writer.writerow(["spam", "eggs", "bacon", "ham"])
output_writer.writerow(["Hello,world!", "eggs", "bacon", "ham"])
output_writer.writerow([1, 2, 3.141592, 4])

output_file.close()


# 인자값 사용하기 (구분자로 tab, 한 행마다 2줄씩 띄우는 파일 생성)
csv_file = open("example.tsv", "w", newline="")
csv_writer = csv.writer(csv_file, delimiter="\t", lineterminator="\n\n")

csv_writer.writerow(["apples", "oranges", "grapes"])
csv_writer.writerow(["eggs", "bacon", "ham"])
csv_writer.writerow(["spam", "spam", "spam", "spam", "spam", "spam"])

csv_file.close()
