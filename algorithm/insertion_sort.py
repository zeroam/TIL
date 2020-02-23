def insertion_sort(arr: list) -> None:
    """삽입 정렬 알고리즘
    각 값이 어떤 위치에 가야할 지 찾음
    :param arr: 정렬할 리스트
    """
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = element


if __name__ == '__main__':
    element_list = [8, 2, 3, 4, 7, 1, 5, 6, 9]
    insertion_sort(element_list)
    print(element_list)