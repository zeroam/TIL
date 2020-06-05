"""find_big_files.py
용량이 지정한 용량 이상인 파일을 찾아 경로 출력
"""
import os
import enum


class SIZE_UNIT(enum.Enum):
    BYTE = 1
    KB = 2
    MB = 3
    GB = 4


def get_keyword(unit: SIZE_UNIT):
    if unit == SIZE_UNIT.BYTE:
        return 'bytes'
    elif unit == SIZE_UNIT.KB:
        return 'KB'
    elif unit == SIZE_UNIT.MB:
        return 'MB'
    elif unit == SIZE_UNIT.GB:
        return 'GB'


def cover_unit(size_in_bytes: int, value: int):
    if value == 0:
        return size_in_bytes

    kilo_bytes = 1024
    return round(size_in_bytes / (kilo_bytes ** value), 3)


def get_file_size(file_path: str, unit: SIZE_UNIT):
    byte_size = os.path.getsize(file_path)
    return cover_unit(byte_size, unit.value - 1)


def find_big_files(src_dir: str, big_size: int = 0, unit: SIZE_UNIT = SIZE_UNIT.BYTE):
    for curfolder, subfolder, filenames in os.walk(src_dir):
        for filename in filenames:
            path = os.path.join(curfolder, filename)
            path = os.path.abspath(path)
            size = get_file_size(path, unit)

            if size > big_size:
                print(f'file: {path}, size: {size} {get_keyword(unit)}')


if __name__ == "__main__":
    find_big_files('C:\\', 100, SIZE_UNIT.MB)
