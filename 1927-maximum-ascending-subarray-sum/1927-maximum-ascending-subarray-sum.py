class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum, max_sum = nums[0], 0
        for i in range(len(nums) - 1):  
            if nums[i] < nums[i + 1]:
                cur_sum += nums[i + 1]
            else:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[i + 1]
        return max(max_sum, cur_sum)
