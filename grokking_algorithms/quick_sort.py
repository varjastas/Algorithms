def quick_sort(array):
    print(array)
    if (len(array) < 2):
        return array
    
    pivot = array[0]

    less = [i for i in array[1:] if i < pivot]
    bigger = [i for i in array[1:] if i > pivot]
    print(less + [pivot] + bigger)
    return quick_sort(less) + [pivot] + quick_sort(bigger)

def tests():
    assert quick_sort([0, 3, 4, 2, 1]) == [0, 1, 2, 3, 4], quick_sort([0, 3, 4, 2, 1])

tests()