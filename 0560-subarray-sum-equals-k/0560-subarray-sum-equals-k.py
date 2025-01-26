class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        p = 0
        p_f = {0: 1} 
        for num in nums:
            p += num 
            if (p - k) in p_f:
                count += p_f[p - k]  
            if p in p_f:
                p_f[p] += 1  
            else:
                p_f[p] = 1          
        return count



