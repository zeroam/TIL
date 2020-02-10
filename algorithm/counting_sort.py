def countSort(array, num_max):
    # create count list
    count = [0 for _ in range(num_max + 1)]
    
    # count
    for num in array:
        count[num] += 1
        
    # accumulate sum
    for i in range(len(count)):
        if i == 0:
            continue
        
        count[i] = count[i - 1] + count[i]

    result = array.copy()
    # insert num
    for i in range(len(result) - 1, -1, -1):
        num = array[i]
        num_index = count[num] - 1
        result[num_index] = num
        count[num] -= 1

    return result
        
    
    
def main():
    array1 = [4, 1, 2, 1, 3, 4, 2, 0]
    assert countSort(array1, 4) == [0, 1, 1, 2, 2, 3, 4, 4]
    print('test 1 passed')

    array2 = [10, 2, 1, 3, 2, 2, 1, 3, 5, 4, 7, 8]
    assert countSort(array2, 10) == [1, 1, 2, 2, 2, 3, 3, 4, 5, 7, 8, 10]
    print('test 2 passwd')


if __name__ == '__main__':
    main()