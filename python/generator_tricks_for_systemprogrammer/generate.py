import math


def generate(func):
    def gen_func(s):
        for item in s:
            yield func(item)

    return gen_func


if __name__ == "__main__":
    gen_sqrt = generate(math.sqrt)
    for x in gen_sqrt(range(100)):
        print(x)
