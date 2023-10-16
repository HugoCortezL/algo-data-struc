def partition(array, low, high):
    pivot = array[(low + high) // 2]

    while True:
        while array[low] < pivot:
            low += 1

        while array[high] > pivot:
            high -= 1

        if low >= high:
            return high

        array[low], array[high] = array[high], array[low]

        low += 1
        high -= 1


def quick_sort_helper(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        quick_sort_helper(array, low, partition_index)
        quick_sort_helper(array, partition_index + 1, high)

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array
