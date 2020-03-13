# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot = my_list[end]
    big_index = start
    
    for i in range(start, end):
        if my_list[i] < pivot:
            swap_elements(my_list, i, big_index)
            big_index += 1
    
    swap_elements(my_list, end, big_index)
    
    return big_index