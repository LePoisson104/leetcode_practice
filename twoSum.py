# easy
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# brute force
def twoSum(nums, target):
    for i, num1 in enumerate(nums):  # get both the index and the value in one loop
        for j, num2 in enumerate(nums):
            if i == j:  # we don't want to return when add itself to get the target
                continue
            elif num1 + num2 == target:
                return [i,j]
    return []

# hash map
def twoSumHash(nums, target):
    hashMap = {}
    for i in range(len(nums)):   # get the index 
        complement = target - nums[i]   # get the difference
        if complement in hashMap:   # if in the hashmap we know that it's the difference
            return [hashMap[complement], i]
        hashMap[nums[i]] = i    # use the difference value as the key and the index as the value
    return []

list1 = [2,7,11,15]
target = 9
result = twoSumHash(list1, target)
print(result)
