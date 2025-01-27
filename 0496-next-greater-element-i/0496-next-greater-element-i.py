class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1 for _ in nums1]
        stack = []
        for i in range(len(nums2)):
            pivot = nums2[i]
            while stack and nums1[stack[-1]] < pivot:
                ans[stack[-1]] = pivot
                stack.pop()       
            if pivot in nums1:
                stack.append(nums1.index(pivot))     
        return ans

            

                



