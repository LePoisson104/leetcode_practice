def isPalindrome(num):
    numStr = str(num)
    tempStr = ""
    for i in range(1, len(numStr)+1):
        tempStr += numStr[len(numStr) - i]
    if numStr == tempStr:
        return True
    return False

num = 121
print(isPalindrome(num));