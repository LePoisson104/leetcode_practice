# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

def mergeTwoList(list1, list2):
    mergeLists = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            mergeLists.append(list1[i])
            i += 1
        elif list1[i] > list2[j]:
            mergeLists.append(list2[j])
            j += 1
        else:  # list1[i] == list2[j]
            mergeLists.append(list1[i])
            mergeLists.append(list2[j])
            i += 1
            j += 1

    # Append the remaining elements from list1 or list2
    if i < len(list1):
        mergeLists.extend(list1[i:])
    if j < len(list2):
        mergeLists.extend(list2[j:])

    return mergeLists

list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(mergeTwoList(list1, list2))


# NOT FINISH
