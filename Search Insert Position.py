def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i+1] > target:
            return i

assert searchInsert([1,3,5,6], 5) == 2
assert searchInsert([1,3,5,6], 2) == 1
assert searchInsert([1,3,5,6], 7) == 4
assert searchInsert([1,3,5,6], 0) == 0