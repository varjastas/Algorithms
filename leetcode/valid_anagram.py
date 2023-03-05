def valid_anagram(first: str, second: str):
    if (len(first) - len(second) != 0):
        return first
    
    used = []

    for i in first:
        if not i in used:
            if first.count(i) != second.count(i):
                return False
            used.append(i)
        
    
    return True
def tests():
    print(valid_anagram("rat", "car"))
    print(valid_anagram("anagram", "nagaram"))

tests()