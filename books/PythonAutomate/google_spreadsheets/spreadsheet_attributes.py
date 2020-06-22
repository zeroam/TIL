"""spreadsheet_attributes.py
구글 스프레드시트 문서 속성 값 접근
"""
import ezsheets

sheet_id = "1FIk-KAb9Ddi03XE2c179-K6Vnnu_wJ2BZLyYOj5G_L4"
ss = ezsheets.Spreadsheet(sheet_id)
print(ss.title)  # 제목 출력
ss.title = "Changed Title"  # 제목 변경
print(ss.url)  # url 링크 출력
print(ss.sheetTitles)  # 해당 문서의 Sheet Title 출력
print(ss.sheets)  # 해당 문서의 Sheet 객체 출력
print(ss[0])  # 첫번째 시트 객체 출력
del ss[2]  # 세번째 시트 삭제
print(ss.sheetTitles)
ss.refresh()  # 변경사항 반영