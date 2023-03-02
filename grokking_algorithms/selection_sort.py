def find_smallest(array):
    if (len(array) == 0):
        return None
    smallest_index = 0
    smallest = array[0]
    for i in range(1, len(array)):
        if (array[i] < smallest):
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    if (len(array) == 0):
        return None
    new_array = []
    for i in range(0, len(array)):
        new_array.append(array.pop(find_smallest(array)))
    return new_array


def tests():
    assert selection_sort([0, 3, 2, 1]) == [0, 1, 2, 3], selection_sort(selection_sort([0, 3, 2, 1]))
    assert selection_sort([]) == None, selection_sort(None)
    assert selection_sort([0, 1, 4, 2, 5, 3, 2, 1]) == [0, 1, 1, 2, 2, 3, 4, 5], selection_sort([0, 1, 4, 2, 5, 3, 2, 1])
tests()