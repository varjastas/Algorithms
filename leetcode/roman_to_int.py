def roman_to_int(roman: str):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    i = 0
    while i < len(roman):
        symbol = roman[i]

        if i == len(roman) - 1:
            result += values[symbol]
        else:
            next_symbol = roman[i + 1]

            if (values[symbol] < values[next_symbol]):
                i += 1
                result += values[next_symbol] - values[symbol]
            else:
                result += values[symbol]
        i += 1

    return result

def tests():
    print(roman_to_int("LVIII"), end="\n\n")
    print(roman_to_int("III"), end="\n\n")
    print(roman_to_int("MCMXCIV"),  end="\n\n")

tests()