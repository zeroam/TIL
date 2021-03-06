#!/bin/env python
import os
import sys
import datetime
from time import sleep

from text_colors import colors
from mylog import get_log_data


def check(file_name, search_word, out_file_name):
    if os.path.exists(file_name):
        print(f"모니터링 시작 : {file_name}")
        print(f"대상 : {search_word}")
        print("-" * 70)
    else:
        print(f"찾으려는 파일이 없습니다 : {file_name}")
        sys.exit(1)

    index = 0
    while os.path.exists(file_name):
        fp = open(file_name)
        file_data = fp.read()
        index = file_data.find(search_word, index)
        fp.close()

        if index >= 0:
            alert(search_word)
            data, _ = get_log_data(file_data, search_word, index, 2, 2)

            out_file = open(out_file_name, "a")
            out_file.write("\n" + ("*" * 70))
            out_file.write(f"\n문제({search_word})가 모니터링 된 시각 : {datetime.datetime.now()}")
            out_file.write("\n" + ("*" * 70))
            out_file.write(data)
            out_file.close()
            print(f"로그가 기록된 파일을 확인하세요: {out_file_name}")
        else:
            print("...", end="", flush=True)

        index = len(file_data)
        sleep(5)


def alert(search_word):
    now = datetime.datetime.now()
    if search_word == "FATAL":
        print(f"{colors.fg.red}\n{now} 심각한 문제가 발생했습니다!!{colors.reset}")
    elif search_word == "except":
        print(f"{colors.fg.yellow}\n{now} 문제가 발생했습니다!!{colors.reset}")


if __name__ == "__main__":
    check("/var/log/syslog", "FATAL", "customized_warn")
