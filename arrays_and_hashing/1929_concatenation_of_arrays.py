# 1929. Concatenation of Arrays
# Given an integer array nums of length n, 
# you want to create an array ans of length 2n where 
# ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#
# Specifically, ans is the concatenation of two nums arrays.
#
# Return the array ans.


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return 2*nums