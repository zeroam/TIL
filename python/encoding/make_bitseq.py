def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in s)


if __name__ == "__main__":
    print(make_bitseq("bits"))
    print(make_bitseq("CAPS"))
    print(make_bitseq("$25.43"))
    print(make_bitseq("~5"))
