def romanToInt(s):
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    total = 0
    skip = False
    for index, char in enumerate(s):
        if skip:
            skip = False
            continue
        elif index+1 != len(s) and roman[char] < roman[s[index+1]]:
            total += roman[s[index+1]] - roman[char]
            skip = True
        elif char in roman:
            total += roman[char]
            
    return total

s = "MCMXCIV"
print(romanToInt(s));