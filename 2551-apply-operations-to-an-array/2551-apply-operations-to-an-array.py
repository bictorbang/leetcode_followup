class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res_1, res_2 = [], []
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            res_1.append(nums[i]) if nums[i] else res_2.append(nums[i])
        res_1.append(nums[n - 1]) if nums[n - 1] else res_2.append(nums[n - 1])
        return res_1 + res_2
            
        