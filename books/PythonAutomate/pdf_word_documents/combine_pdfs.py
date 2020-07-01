"""combine_pdfs.py
많은 PDF파일들의 첫페이지를 제외한 페이지들을 합쳐 하나의 파일로 만들기
"""
import os
import PyPDF2
from pathlib import Path

# meetingminutes으로 시작하는 pdf 파일 리스트 조회
pdf_files = list(Path(".").rglob("meetingminutes*.pdf"))
pdf_files.sort(key=lambda x: str(x).lower())

pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for pdf_path in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(pdf_path.open("rb"))

    # Loop through all the pages (except the first) and add them
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

# Save the resulting PDF to a file
pdf_output = open("allminutes.pdf", "wb")
pdf_writer.write(pdf_output)
pdf_output.close()
