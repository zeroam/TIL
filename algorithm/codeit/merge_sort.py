from merge import merge


def merge_sort(my_list):
    size = len(my_list)
    if size <= 1:
        return my_list
    
    mid = size // 2
    left_half = merge_sort(my_list[:mid])
    right_half = merge_sort(my_list[mid:])
    
    return merge(left_half, right_half)

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
