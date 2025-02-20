class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        for i in range(n - 1):
            if not (nums[i] + nums[i + 1])%2: return False
        return True