class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = nums[0]
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum