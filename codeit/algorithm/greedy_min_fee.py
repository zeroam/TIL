def min_fee(pages_to_print):
    sorted_pages_to_print = sorted(pages_to_print)

    total_fee = 0
    while sorted_pages_to_print:
        size = len(sorted_pages_to_print)
        minute = sorted_pages_to_print.pop(0)
        total_fee += size * minute

    return total_fee


if __name__ == '__main__':
    from util import test_value

    test_value(min_fee([6, 11, 4, 1]), 39)
    test_value(min_fee([3, 2, 1]), 10)
    test_value(min_fee([3, 1, 4, 3, 2]), 32)
    test_value(min_fee([8, 4, 2, 3, 9, 23, 6, 8]), 188)