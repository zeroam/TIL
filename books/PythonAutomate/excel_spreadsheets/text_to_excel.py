"""text_to_excel.py
다수의 텍스트 파일을 엑셀 파일로 변환
ex) python text_to_excel.py <텍스트파일 1, 2, 3...>
"""
import sys
import openpyxl

if len(sys.argv) < 2:
    print(f"python {__file__} <text files...>")

wb = openpyxl.Workbook()
sheet = wb.active
for file_index, file_name in enumerate(sys.argv[1:]):
    with open(file_name) as f:
        for i, line in enumerate(f.readlines()):
            sheet.cell(row=i + 1, column=file_index + 1).value = line

wb.save("merged.xlsx")
