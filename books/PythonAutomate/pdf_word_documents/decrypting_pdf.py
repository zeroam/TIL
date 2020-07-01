"""decrypting_pdf.py
암호 걸린 PDF 파일 열기
"""
import PyPDF2

pdf_reader = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))
print(pdf_reader.isEncrypted)  # 암호화 여부 확인

try:
    pdf_reader.getPage(0)  # 페이지 객체 얻기, 에러 발생
except PyPDF2.utils.PdfReadError as e:
    print("ERROR:", e)

pdf_reader = PyPDF2.PdfFileReader(open("encrypted.pdf", "rb"))
pdf_reader.decrypt("rosebud")  # 암호 입력
page_obj = pdf_reader.getPage(0)
print(page_obj)
