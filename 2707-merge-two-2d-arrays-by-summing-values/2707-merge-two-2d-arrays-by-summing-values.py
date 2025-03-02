class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        hm = defaultdict(int)

        for elt in nums1:
            hm[elt[0]] += elt[1]
        for elt in nums2:
            hm[elt[0]] += elt[1]
        for k, v in sorted(hm.items()):
            res.append([k, v])

        return res

