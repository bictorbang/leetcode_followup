class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c1, c2 = 0, 0
        for n in nums:
            if n < 0:
                c1 += 1
            elif n > 0: c2 += 1
        return max(c1, c2)