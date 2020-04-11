"""Clean Code in Python - Chapter 07: Using generators

> search nested
"""
from log import logger


def search_nested_bad(array, desired_value):
    coords = None
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == desired_value:
                coords = (i, j)
                break

        if coords is not None:
            break

    if coords is None:
        raise ValueError(f"{desired_value} not found")

    logger.info("[%i %i]에서 값 %r 찾음", *coords, desired_value)
    return coords


def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, cell in enumerate(row):
            yield (i, j), cell


def search_nested(array, desired_value):
    try:
        coords = next(
            coords
            for (coords, cell) in _iterate_array2d(array)
            if cell == desired_value
        )
    except StopIteration:
        raise ValueError(f"{desired_value} not found")

    logger.info("[%i %i]에서 값 %r 찾음", *coords, desired_value)
1    return coords
