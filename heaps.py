# 215. Kth Largest Element in an Array
def findKethLargest(nums, k):
    nums.sort()

    return nums[-k]
