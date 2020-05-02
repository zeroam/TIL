from merge_sort import merge
from random import randint
from sorting_timer import run_sorting_algorithm, ARRAY_LENGTH


def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    # Loop from the element indicated by
    # `left` unitil the element indicated by `right`
    for i in range(left + 1, right + 1):
        # This is the element we want to position in tis
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if the `key_item` is smaller than its adjacent values.
        while j >= left and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition `j` to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, position
        # the `key_item` in its correct location
        array[j + 1] = key_item

    return array


def timesort(array):
    min_run = 32
    n = len(array)

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + `, while the `right` array should
            # go from `midpoint + 1` to `end + 1`
            merged_array = merge(
                left=array[start:midpoint],
                right=array[midpoint + 1:end + 1]
            )

            # Finally, put the merged array back into
            # your array
            array[start: start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2

    return array


if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    run_sorting_algorithm(algorithm="timesort", array=array)
