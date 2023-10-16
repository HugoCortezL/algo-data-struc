def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return -1