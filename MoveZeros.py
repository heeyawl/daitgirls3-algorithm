from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        e = len(nums)
        for i in range(e):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
        return nums

assert Solution().moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]




# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         #moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         l = len(nums)
#         n = 0
#         while n :
#             for i in range(l):
#                 if nums[i] == 0:
#                     nums.remove(0)
#                     nums[e] == 0
#         return nums
#
# if __name__=='__main__':
#     Solution().moveZeroes([0,1,0,3,12])


# ## solution without class
# def moveZeroes():
#     e = len(nums)
#     for i in range(e):
#         if nums[i] == 0:
#             nums.remove(0)
#             nums[e] = 0
#     return nums
#
# assert moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]
