# 2. Add two numbers
def twoSum(nums, target):
    for i, num in enumerate(nums):
        value = target - num

        if value in nums[i+1:]:
            return [i, nums.index(value, i+1)]
