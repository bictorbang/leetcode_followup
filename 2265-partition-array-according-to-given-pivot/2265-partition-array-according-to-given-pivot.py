class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller, eq, greater = [], [], []
        for elt in nums:
            if elt < pivot: smaller.append(elt)
            elif elt > pivot: greater.append(elt)
            else: eq.append(elt)
        return smaller + eq + greater
