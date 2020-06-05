# Rough implementation of reduce(), taken from Python official documentation:
# https://docs.python.org/3/library/functools.html#functools.reduce


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer

    for element in it:
        value = function(value, element)

    return value


if __name__ == "__main__":
    multipliers = [2, 10, 4, 16]
    accumulation = reduce(lambda acc, number: acc * number, multipliers)
    print(accumulation)
