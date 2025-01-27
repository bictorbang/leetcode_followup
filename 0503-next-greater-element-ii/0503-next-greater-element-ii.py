class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        for n_0 in range(N):
            pivot = nums[n_0]
            n = n_0
            while pivot >= nums[n]: 
                n+=1
                n%=N
                if n == n_0:
                    res.append(-1)
                    break
            if n!=n_0:
                res.append(nums[n])
                
        return res

                    


        res = []
        stack = []
        mapping = {}
        for n in nums2:
            while stack and n > stack[-1]:
                mapping[stack.pop()] = n
            stack.append(n)
        return [mapping.get(n, -1) for n in nums1]