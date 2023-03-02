
def compress(chars):
    if (len(chars) == 1):
        return len(chars[0])
    
    result = ""
    used_char = ""
    counterr = 0
    for i in chars:

        if i == used_char:
            continue
        group_length = 0

        for j in chars[counterr:]:
            if j == i:
                group_length += 1
                counterr += 1
            else:
                break
        if (group_length == 1):
            result += i
        else:
            result += i + str(group_length)
        used_char = i
        
    counter = 0
    for i in result:
        if (counter < len(chars)):
            chars[counter] = i
            counter += 1
        else: 
            chars.append(i)
    
    return len(result)


def tests():
    chars = ["a","a","b","b","c","c","c"]
    print(compress(chars))
    print(chars)

    chars = ["a"]
    print(compress(chars))
    print(chars)

    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(compress(chars))
    print(chars)

tests()