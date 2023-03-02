
def binary_search(array, element):
    if (len(array) == 0):
        return None

    high = len(array) - 1
    low = 0
    while low <= high:
        mid = (low + high) //2

        if array[mid] == element:

            return mid
        elif array[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    return None

def tests():
    assert (binary_search([1, 2, 3, 4, 5, 6], 2) == 1), binary_search([1, 2, 3, 4, 5, 6], 2)
    assert binary_search([1], 1) == 0, binary_search([1], 1)
    assert binary_search([], 2) == None, binary_search([], 2)
    assert binary_search([1], 2) == None, binary_search([1], 2)
    assert binary_search([1, 2, 3], 3) == 2, binary_search([1, 2, 3], 3)
    assert binary_search([1, 2], 2) == 1, binary_search([1, 2], 2)
    

tests()
