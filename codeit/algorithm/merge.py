def merge(list1, list2):
    result = list()
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result += list1 + list2

    return result


if __name__ == '__main__':
    print(merge([1], []))
    print(merge([],[1]))
    print(merge([2],[1]))
    print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
    print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
    print(merge([4, 7, 8, 9],[1, 3, 6, 10]))