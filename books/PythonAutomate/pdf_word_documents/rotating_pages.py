"""rotating_pages.py
페이지 회전하기
"""
import PyPDF2

minutes_file = open("meetingminutes.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(minutes_file)

page = pdf_reader.getPage(0)
page.rotateClockwise(90)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page)

result_pdf_file = open("rotated_page.pdf", "wb")
pdf_writer.write(result_pdf_file)

result_pdf_file.close()
minutes_file.close()
