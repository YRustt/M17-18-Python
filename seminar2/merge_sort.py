
def merge(left_array, right_array):
    merge_array = []

    while left_array and right_array:
        if left_array[-1] > right_array[-1]:
            merge_array.append(left_array.pop())
        else:
            merge_array.append(right_array.pop())

    return (merge_array + left_array + right_array)[::-1]


def sort(array):
    if len(array) < 2:
        return array

    mid_idx = len(array) // 2
    result = merge(list(sort(array[:mid_idx])), list(sort(array[mid_idx:])))
    return result if isinstance(array, list) else tuple(result)
