"""brute_force.py
dictionary.txt 파일을 이용해
암호 문서 해제하기
"""
import sys
import PyPDF2
import multiprocessing
from time import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed


def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished in {time() - start_time:.2f}")
        return result

    return wrapper



# @elapsed_time
def find_password(filepath: str, passwords: list):
    for password in passwords:
        try:
            pdf_reader = PyPDF2.PdfFileReader(open(filepath, "rb"))
            pdf_reader.decrypt(password.upper())
            pdf_reader.decrypt(password.lower())
            # print(f"checking {password}")
            pdf_reader.getPage(0)
            return password
        except PyPDF2.utils.PdfReadError as e:
            pass


# @elapsed_time
def find_password_binary(filepath: str, passwords: list, result: list=[]):
    try:
        pdf_reader = PyPDF2.PdfFileReader(open(filepath, "rb"))
        for password in passwords:
            pdf_reader.decrypt(password.upper())
            pdf_reader.decrypt(password.lower())
        pdf_reader.getPage(0)
        # print(f"password list: {passwords}")
        size = len(passwords)
        if size == 1:
            result.append(passwords[0])
        else:
            find_password_binary(filepath, passwords[:size // 2], result)
            find_password_binary(filepath, passwords[size // 2:], result)
        return result[0]
    except PyPDF2.utils.PdfReadError as e:
        return None

@elapsed_time
def decrypt_pdf(filepath: str, password_txt: str) -> None:
    with open(password_txt) as f:
        passwords = f.read().split("\n")

    pdf_reader = PyPDF2.PdfFileReader(open(filepath, "rb"))
    if not pdf_reader.isEncrypted:
        print(f"{filepath} is not encrypted")
        return

    # CPU 갯수 * 2 만큼 리스트 쪼개기
    concurrent_limit = multiprocessing.cpu_count() * 2
    size = len(passwords) // concurrent_limit
    remain = len(passwords) % concurrent_limit
    split_lists = []
    for i in range(concurrent_limit):
        split_lists.append(passwords[size * i: size * (i + 1)])
    split_lists[-1].extend(passwords[-remain:])

    with ProcessPoolExecutor(max_workers=concurrent_limit) as executor:
        future_to_password = {executor.submit(find_password_binary, filepath, split): split for split in split_lists}
        for future in as_completed(future_to_password):
            password = future_to_password[future]
            try:
                result = future.result()
            except Exception as exc:
                print(f"generated excetpion: {exc}")
            else:
                if result is not None:
                    print(f"password is : {result}")


if __name__ == "__main__":
    decrypt_pdf("encrypted.pdf", "dictionary_origin.txt")  # 대략 220초 소요(cpu: 6)
