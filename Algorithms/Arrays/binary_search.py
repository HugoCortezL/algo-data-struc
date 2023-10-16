def is_sorted(array):
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


def rec_binary_search(array, start, end, target):
    if not array or start > end:
        return -1

    mid = start + (end - start) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return rec_binary_search(array, mid+1, end, target)
    else:
        return rec_binary_search(array, start, mid-1, target)


def recursive_binary_search(array, target):
    if not is_sorted(array):
        raise ValueError("The array must be sorted.")

    return rec_binary_search(array, 0, len(array)-1, target)


def binary_search(array, target):
    if not is_sorted(array):
        raise ValueError("The array must be sorted.")
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


a = [1, 4, 6, 8, 10, 15, 20, 24, 36, 47, 60]
t = recursive_binary_search(a, 3)
print(t)
