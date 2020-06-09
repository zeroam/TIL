"""map_it.py
인자값 또는 클립보드 값으로 검색한 구글 맵 브라우저 실행
"""
import sys
import webbrowser
import pyperclip


def main():
    if len(sys.argv) > 1:
        address = ''.join(sys.argv[1:])
    else:
        # Get address from clipboard
        address = pyperclip.paste()

    webbrowser.open(f"https://www.google.com/maps/place/{address}")


if __name__ == "__main__":
    main()
