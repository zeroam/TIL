"""encrypting_pdf.py
PDF 파일 암호화 하기
"""
import PyPDF2

pdf_file = open("meetingminutes.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_writer = PyPDF2.PdfFileWriter()

# PDF 복사
for page_num in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(page_num))

# PDF 암호화
pdf_writer.encrypt("swordfish")

result_pdf = open("encryptedminutes.pdf", "wb")
pdf_writer.write(result_pdf)
result_pdf.close()
