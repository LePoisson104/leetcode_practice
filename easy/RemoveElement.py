def removeElement(nums, val):
    prevVals = []
    newList = []
    for i, num in enumerate(nums):
        if num == val:
            continue
        elif num == val and i < len(nums) and nums[i+1] != val:
            prevVals.append(nums[i])

    return len(newList), prevVals

nums = [3,2,2,3,1,3,2,3]
val = 3
print(removeElement(nums,val))