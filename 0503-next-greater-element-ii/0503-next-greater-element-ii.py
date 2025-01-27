class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N
        stack = []
        for i, elt in enumerate(nums):
            while stack and elt > nums[stack[-1]]:
                res[stack.pop()] = elt
            stack.append(i)
        for elt in nums:
            while stack and elt > nums[stack[-1]]:
                res[stack.pop()] = elt            
        return res