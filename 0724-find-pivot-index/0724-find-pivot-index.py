class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        suffix = sum(nums)
        for i in range(len(nums)):
            suffix -= nums[i]
            if prefix == suffix:
                return i
            prefix += nums[i]

        return -1