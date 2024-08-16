def longestCommonPrefix(strList):
    result = ""
    sortedList = sorted(strList) # sort the list in alphabetical order
    first = sortedList[0]
    last = sortedList[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return result
        result += first[i]
    return result

strs = ["flowers", "flow", "flight"]
print(longestCommonPrefix(strs))