def selection_sort(arr: list) -> None:
    """선택정렬 알고리즘
    각 위치에 어떤 값이 들어갈 지 찾음
    :param arr: 정렬할 배열
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(min_index + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    element_list = [5, 2, 3, 1, 4, 7, 9]

    selection_sort(element_list)
    print(element_list)
    assert element_list == [1, 2, 3, 4, 5, 7, 9], "Wrong Sorting"
