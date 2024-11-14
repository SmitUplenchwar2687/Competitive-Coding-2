def twosum(nums, target):
    res = {}
    for i in range(len(nums)):
        res[nums[i]] = i
    for i in range(len(nums)):
        if target-nums[i] in res:
            return i, res[target-nums[i]]
    return -1

nums = [2,5,9,12,6]
target = 15

print(twosum(nums,target))