import os
import shutil
from pathlib import Path




def main():
    dir_name = 'dates_sample'
    filenames = [
        'spam4-4-1984.txt',
        '01-03-2014eggs.zip',
        '06-02-2020today.txt',
        '6-2-2020cur.pdf',
        'littlebrother.epub'
    ]

    # 기존 파일들 삭제
    if os.path.isdir(dir_name):
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

    for filename in filenames:
        # 빈 파일 생성
        open(os.path.join(dir_name, filename), 'a').close()


if __name__ == "__main__":
    main()