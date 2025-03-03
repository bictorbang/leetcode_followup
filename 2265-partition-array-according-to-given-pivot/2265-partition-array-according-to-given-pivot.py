class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s, eq, g = [], [], []
        for i in nums:
            if i < pivot: s.append(i)
            elif i > pivot: g.append(i)
            else: eq.append(i)
        return s + eq + g
