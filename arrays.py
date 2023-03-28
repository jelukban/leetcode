# 2. Add two numbers
def twoSum(nums, target):
    for i, num in enumerate(nums):
        value = target - num

        if value in nums[i+1:]:
            return [i, nums.index(value, i+1)]


# 283. Move Zeroes
def moveZeroes(nums):
    num_of_zeroes = 0

    while 0 in nums:
        num_of_zeroes += 1
        nums.remove(0)

    for i in range(0, num_of_zeroes):
        nums.append(0)
