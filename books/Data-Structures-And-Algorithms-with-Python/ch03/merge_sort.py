def mergeSort(nums):
    # base case if the input array is one or zero just return
    if len(nums) > 1:
        # splitting input array
        print('splitting', nums)
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        # recursive calls to mergeSort for left and right subarrays
        mergeSort(left)
        mergeSort(right)
        # initializes pointers for left(i) right(j) and output array (k)

        # 3 initialziing operations
        i = j = k = 0
        # Traverse and merge the sorted arrays
        while i < len(left) and j < len(right):
            # if left < right comparison operation
            if left[i] < right[j]:
                nums[k] = left[i]
                i = i + 1
            else:
                # if right <= left assignment
                nums[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            nums[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            nums[k] = right[j]
            j = j + 1
            k = k + 1

    print('merging', nums)
    return nums


if __name__ == '__main__':
    mergeSort([356, 97, 846, 215])