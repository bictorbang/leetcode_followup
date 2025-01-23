# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums 
# except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed 
# to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without 
# using the division operation.

from typing import List

# Date: 24.01.2025
# Runtime: 27ms (49.76%)
# Memory: 23.23MB (66.93%)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        product = 1
        for i in range(len(nums)): # prefix
            output[i] *= product
            product *= nums[i]
        
        product = 1
        for i in reversed(range(len(nums))): # suffix
            output[i] *= product
            product *= nums[i]
    
        return output   