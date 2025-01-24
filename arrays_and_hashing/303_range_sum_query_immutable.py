# 303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries 
# of the following type:
#
# Calculate the sum of the elements of nums between 
# indices left and right inclusive where left <= right.
# 
# Implement the NumArray class:
#
# NumArray(int[] nums)              Initializes the object with 
#                                   the integer array nums.
#
# int sumRange(int left, int right) Returns the sum of the elements of nums
#                                   between indices left and right 
#                                   inclusive (i.e. nums[left] + 
#                                   nums[left + 1] + ... + nums[right]).

from typing import List

# Date: 24.01.2025
# Runtime: 714ms
# Memory: 21.50MB
#
# Naive implementation. One-liner, but this is suboptimal.

class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.a[left:right+1])
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# Date: 24.01.2025
# Runtime: 0ms
# Memory: 21.60MB
#
# A more efficient approach is to directly store the sums.

class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] # Also changes a (lists are immutable)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.a[right]
        return self.a[right] - self.a[left - 1]