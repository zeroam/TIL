"""pdf_extract_text.py
PDF 특정 페이지의 텍스트 추출하기
"""
import PyPDF2

pdf_file_obj = open("meetingminutes.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
print(pdf_reader.numPages)  # 페이지 갯수 출력
page_obj = pdf_reader.getPage(0)  # 첫 번째 페이지 객체
print(page_obj.extractText())  # 텍스트 추출
pdf_file_obj.close()
