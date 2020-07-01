"""sum_spreadsheets.py
A, B 열에 있는 데이터를 더해
삽입한 C열에 결과 업데이트
"""
import ezsheets


sheet_id = "1kE8mgP-GKx8HJKHNhHfOLeZaWZCSBo2v4D3vwzKwipw"
ss = ezsheets.Spreadsheet(sheet_id)
sheet = ss[0]

rows = sheet.getRows()

column_count = sheet.columnCount
for i in range(column_count, 2, -1):
    sheet.updateColumn(i + 1, sheet.getColumn(i))

update_list = []
for i, row in enumerate(rows):
    x = row[0]
    y = row[1]
    if i == 0:
        update_list.append("TOTAL")
        continue
    if x.isdigit() and y.isdigit():
        update_list.append(eval(f"{x}+{y}"))
    else:
        update_list.append("")

sheet.updateColumn(3, update_list)
