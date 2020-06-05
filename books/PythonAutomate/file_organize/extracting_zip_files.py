import os
import zipfile
from pathlib import Path

p = Path('.')
example_zip = zipfile.ZipFile(p / 'example.zip')

# 전부 압축 풀기
example_zip.extractall('example')

# 단일 파일 풀기
example_zip.extract('spam.txt')
example_zip.extract('cats/catnames.txt', 'new_folder')

example_zip.close()