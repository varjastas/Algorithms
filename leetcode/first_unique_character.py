def get_unique(string : str):
    used = []
    counter = 0
    for i in string:
        if not i in used:
            if string.count(i) == 1:
                return counter
        else:
            counter += 1
            continue
        used.append(i)
        counter += 1

    return -1

def tests():
    print(get_unique("loveleetcode"))
    print(get_unique("aabb"))
    print(get_unique("leetcode"))

tests()