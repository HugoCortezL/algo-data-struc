def selection_sort(array):
    for i in range(len(array)):
        min_value = array[i]
        min_index = i

        for j in range(i, len(array)):
            if array[j] < min_value:
                min_value = array[j]
                min_index = j
                
        array[i], array[min_index] = array[min_index], array[i]
    return array