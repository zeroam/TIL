"""read_write_data.py
구글 스프레드 시트 문서에 데이터 입력 및 접근하기
"""
import ezsheets

ss = ezsheets.createSpreadsheet("My SpreadSheet")
sheet = ss[0]  # 첫번째 시트에 접근
print(sheet.title)  # '시트1'

# 데이터 입력
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["C1"] = "Favorite Movie"

print(sheet["A1"])  # Name
print(sheet[2, 1])  # Age

sheet[1, 2] = "Alice"
sheet[2, 2] = 30
sheet[3, 2] = "RoboCop"


# 특정 행, 열 접근하기
print(sheet.getRow(1))  # 첫 번째 행 접근
print(sheet.getColumn(1))  # 첫 번째 열 접근하기
# print(sheet.getColumn("A"))  # 첫 번째 열 접근하기


# 특정 행, 열 수정하기
sheet.updateRow(3, ["Pumpkin", 25, "Halloween"])

column_one = sheet.getColumn(1)
for i, value in enumerate(column_one):
    column_one[i] = value.upper()
sheet.updateColumn(1, column_one)  # 대문자로 변환된 리스트로 수정 내용 반영


# 모든 데이터 접근하기
rows = sheet.getRows()
print(rows[0])  # 첫 번째 행 데이터
rows[3][0] = "NewName"
sheet.updateRows(rows)
