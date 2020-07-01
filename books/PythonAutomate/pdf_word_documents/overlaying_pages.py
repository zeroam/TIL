"""overlaying_pages.py
워터마크 넣기
"""
import PyPDF2

pdf_reader = PyPDF2.PdfFileReader(open("meetingminutes.pdf", "rb"))
minutes_first_page = pdf_reader.getPage(0)

pdf_watermark_reader = PyPDF2.PdfFileReader(open("watermark.pdf", "rb"))
minutes_first_page.mergePage(pdf_watermark_reader.getPage(0))  # 페이지 겹치기

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(minutes_first_page)

for page_num in range(1, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

result_pdf_file = open("watermartedCover.pdf", "wb")
pdf_writer.write(result_pdf_file)
result_pdf_file.close()
