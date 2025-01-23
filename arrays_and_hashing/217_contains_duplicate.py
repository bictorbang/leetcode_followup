# 217. Contains Duplicate
# Given an integer array nums, return true if any value 
# appears at least twice in the array, and return false 
# if every element is distinct.

from typing import List

# Date: 23.01.2025
# Runtime: 4ms (90.77%)
# Memory: 31.54MB (43.04%)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)