"""selective_search.py
선택적 복사 
- 인자로 받은 확장자로 끝나는 파일을 지정한 디렉터리에 저장
"""
import os
import sys
import shutil
from pathlib import Path


def copy(format, dest_dir="new"):
    cur_dir = Path.cwd()
    dir_path = Path(dest_dir).absolute()
    dir_path.mkdir(exist_ok=True)

    for path in cur_dir.rglob(f"**/*.{format}"):
        dest = dir_path / path.name
        if path != dest:
            print(f"copying {path.relative_to(cur_dir)} to {dest.relative_to(cur_dir)}")
            shutil.copy(path, dest_dir)


def main():
    if len(sys.argv) < 2:
        print(f"python {__file__} [ext]")
        return

    copy(sys.argv[1])


if __name__ == "__main__":
    main()
