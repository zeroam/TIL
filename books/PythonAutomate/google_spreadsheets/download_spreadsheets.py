"""download_spreadsheets.py
구글 스프레드시트 문서 다운로드
"""
import os
import ezsheets

sheet_id = "1FIk-KAb9Ddi03XE2c179-K6Vnnu_wJ2BZLyYOj5G_L4"
ss = ezsheets.Spreadsheet(sheet_id)
os.makedirs('down', exist_ok=True)
ss.downloadAsExcel('down/data.xlsx')  # 엑셀 파일로 다운로드
ss.downloadAsODS('down/data.ods')  # OpenOffice 파일로 다운로드
ss.downloadAsCSV('down/data.csv')  # CSV 파일로 다운로드
ss.downloadAsTSV('down/data.tsv')  # TSV 파일로 다운로드
ss.downloadAsPDF('down/data.pdf')  # PDF 파일로 다운로드
ss.downloadAsHTML('down/data.zip')  # HTML 파일들의 zip 파일로 다운로드
