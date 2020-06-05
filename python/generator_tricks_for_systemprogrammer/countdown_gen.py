def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


if __name__ == "__main__":
    x = countdown(10)  # No output
    print(x)  # return generator

    # functions starts executing here
    x.__next__()
