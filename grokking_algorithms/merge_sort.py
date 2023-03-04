def merge_sort(array):
    if len(array) < 2:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def tests():
    print(merge_sort([1, 3, 2, 4, 5, 6, 7, 8, 9, 10]))
    print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(merge_sort([1]))
    print(merge_sort([2, 1]))
    print(merge_sort([]))


if __name__ == '__main__':  
    tests()