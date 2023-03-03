def shortest_palindrome(s : str):
    q = []
    i = 0 
    while(not is_palindrome("".join(q) + s)):
        q.append(s[-1 - i] )
        i += 1
    return "".join(q) + s

def is_palindrome(s):
    return s == s[::-1]

def tests():
    print(shortest_palindrome("abbacd"))
    print(shortest_palindrome("abcd"))

tests()