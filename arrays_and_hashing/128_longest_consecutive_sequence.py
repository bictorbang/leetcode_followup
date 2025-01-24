# 128. Longest Consecutive Sequence
# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
#
#You must write an algorithm that runs in O(n) time.

from typing import List

# Date: 24.01.2025
# Runtime: 43ms (82.97%)
# Memory: 34.32MB (26.31%)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nums:
                length = 1

                while n + length in nums:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
    
# Clever (?) solution (not mine). I found it elegant so I saved it.
# Runtime: 122ms (30.47%)
# Memory: 45.27MB (5.09%)
#
# Uses a dictionary where each key represents a number from 
# the input array, and its corresponding value indicates the length 
# of a consecutive sequence with that number as either 
# the upper or lower bound of the sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            prev = table.get(num - 1, 0)
            next = table.get(num + 1, 0)
            val = prev + next + 1
            table[num - prev] = val
            table[num + next] = val
            maxval = max(maxval, val)
        return maxval