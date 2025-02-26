class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minsum, maxsum = 0, 0
        for elt in nums:
            maxsum = max(0, maxsum + elt)
            minsum = min(0, minsum + elt) 
        return maxsum-minsum