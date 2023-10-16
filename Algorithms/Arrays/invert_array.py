def invert_array(array):
    if len(array) == 0:
        return array
    start = 0
    end = len(array) - 1
    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array