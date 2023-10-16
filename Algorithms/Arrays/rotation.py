def rotation_right(array, times):
    if len(array) == 0:
        return array
    
    times = times % len(array)

    left = array[:-times]
    right = array[-times:]

    return right + left

def rotation_left(array, times):
    if len(array) == 0:
        return array
    
    times = times % len(array)

    left = array[:times]
    right = array[times:]

    return right + left