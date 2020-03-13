def max_product(card_lists):
    max_product = 1

    for card_list in card_lists:
        max_product *= max(card_list)

    return max_product


if __name__ == '__main__':
    from util import test_value

    test_cards1 = [[1, 6, 5], [4, 2, 3]]
    test_value(max_product(test_cards1), 24)

    test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
    test_value(max_product(test_cards2), 244944)

    test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
    test_value(max_product(test_cards3), 10800)

    test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
    test_value(max_product(test_cards4), 12600)