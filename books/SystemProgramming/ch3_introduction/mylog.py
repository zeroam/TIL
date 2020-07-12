#!/bin/env python
def printlog(logfile, search_word, start_index, pre_rowcount, next_rowcount):
    f = open(logfile)
    logdata = f.read()
    f.close()

    index = logdata.find(search_word, start_index)

    if index >= 0:
        print("-" * 70)
        print(f"Log file : {logfile}")
        print(f"Find this word : {search_word}")
        print("-" * 70)

        data, count = get_log_data(logdata, search_word, index, pre_rowcount, next_rowcount)
        print(data)
        print(f"추출한 로그 개수: {count}")

        print("-" * 70)


def get_log_data(logdata, search_word, start_index, pre_rowcount, next_rowcount):
    count = 0
    delimeter = "\n" + ("-" * 70)
    ret = [delimeter]

    while start_index >= 0:
        # start_index 앞에 있는 개행문자 인덱스 찾기 (역방향)
        enter_index = max(0, logdata.rfind("\n", 0, start_index))
        for _ in range(0, pre_rowcount):
            enter_index = max(0, logdata.rfind("\n", 0, enter_index))

        # start_index 뒤에 있는 개행문자 인덱스 찾기
        enter_index2 = logdata.find("\n", start_index, len(logdata))
        for _ in range(0, next_rowcount):
            next_end_index2 = logdata.find("\n", enter_index2 + 1, len(logdata))
            if next_end_index2 == -1:
                next_end_index2 = enter_index2
                break
            else:
                enter_index2 = next_end_index2

        data = logdata[enter_index:enter_index2]
        ret.append(data)
        ret.append(delimeter)

        start_index = logdata.find(search_word, enter_index2 + 1)
        count += 1

    return "".join(ret), count
