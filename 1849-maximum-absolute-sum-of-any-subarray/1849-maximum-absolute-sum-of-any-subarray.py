class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_sum, minsum, maxsum = 0, 0, 0
        for elt in nums:
            cur_sum += elt
            maxsum = max(maxsum, cur_sum)
            minsum = min(minsum, cur_sum) 
        return maxsum-minsum