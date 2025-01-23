# 1. Two Sum
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#
#You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#
#You can return the answer in any order.

from typing import List

# Solution1 (23.01.2025)
# Runtime: 1761ms (23.09%)
# Memory: 18.28MB (80.33%)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: return i, j

# Solution2 (23.01.2025)
# Runtime: 0ms (100%) 
# Memory: 18.91MB (22.62%)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            t_ni = target - nums[i]
            if t_ni not in idx:
                idx[nums[i]] = i
            else:
                return (i, idx[t_ni])