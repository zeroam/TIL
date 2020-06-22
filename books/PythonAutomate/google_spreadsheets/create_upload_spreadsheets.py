"""create_upload_spreadsheets.py
구글 스프레드 시트 문서 열기, 생성하기, 업로드 하기
"""
import ezsheets

# 등록된 문서 열기
sheet_id = "1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg"
ss = ezsheets.Spreadsheet(sheet_id)
print(ss)   # <Spreadsheet title="Bean Count", 1 sheets>
print(ss.title)  # Bean Count


# 빈 스프레드 시트 문서 만들기
ss = ezsheets.createSpreadsheet("Title of My New Spreadsheet")
print(ss.title)  # Title of My New Spreadsheet
ss.delete()  # 스프레드 시트 삭제하기


# 이미 존재하는 엑셀 문서 업로드
ss = ezsheets.upload("example.xlsx")
print(ss.title)