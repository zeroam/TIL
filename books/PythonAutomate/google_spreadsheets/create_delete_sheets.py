"""create_delete_sheets.py
구글 스프레드시트 문서 시트 생성 및 삭제 
"""
import ezsheets

ss = ezsheets.createSpreadsheet("Multiple Sheets")
print(ss.sheetTitles)  # ("시트1",)

# 시트 생성
ss.createSheet("Spam")
ss.createSheet("Eggs")
print(ss.sheetTitles)  # ("시트1", "Spam", "Eggs")
ss.createSheet("Bacon", 0)
print(ss.sheetTitles)  # ("Bacon", "시트1", "Spam", "Eggs")

# 시트 삭제
ss[1].delete()
print(ss.sheetTitles)  # ("Bacon", "Spam", "Eggs")
ss["Eggs"].delete()
print(ss.sheetTitles)  # ("Bacon", "Spam")

# 시트 데이터 초기화
ss[0].clear()
