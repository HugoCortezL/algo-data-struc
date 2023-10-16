def bubble_sort(array):
    has_change = True
    while has_change:
        has_change = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i+1], array[i]
                has_change = True
    return array
