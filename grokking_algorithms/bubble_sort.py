def bubble_sort(array: list):
    if (len(array) == 0):
        return None

    for i in range(0, len(array)):
        for j in range(0, len(array) - i - 1):
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def tests():
    assert bubble_sort([0, 3, 2, 1]) == [0, 1, 2, 3], bubble_sort([0, 3, 2, 1])
    assert bubble_sort([0, 1, 4, 2, 5, 3, 2, 1]) == [0, 1, 1, 2, 2, 3, 4, 5], bubble_sort([0, 1, 4, 2, 5, 3, 2, 1])

tests()