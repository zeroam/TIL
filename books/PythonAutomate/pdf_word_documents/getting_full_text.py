"""getting_full_text.py
워드 문서 전체 텍스트 얻기
"""
import docx


def get_text(filename: str) -> str:
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    return "\n".join(full_text)


if __name__ == "__main__":
    filename = "demo.docx"
    print(get_text(filename))
