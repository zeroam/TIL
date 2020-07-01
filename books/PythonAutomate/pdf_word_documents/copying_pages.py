"""copying_pages.py
두 PDF 파일의 페이지를 합친
새로운 PDF 파일 생성"""
import PyPDF2

pdf_file1 = open("meetingminutes.pdf", "rb")
pdf_file2 = open("meetingminutes2.pdf", "rb")

pdf_reader1 = PyPDF2.PdfFileReader(pdf_file1)
pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)
pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf_reader1.numPages):
    page_obj = pdf_reader1.getPage(page_num)
    pdf_writer.addPage(page_obj)

for page_num in range(pdf_reader2.numPages):
    page_obj = pdf_reader2.getPage(page_num)
    pdf_writer.addPage(page_obj)

pdf_output_file = open("combinedminutes.pdf", "wb")
pdf_writer.write(pdf_output_file)  # 디스크에 저장

pdf_output_file.close()
pdf_file1.close()
pdf_file2.close()
