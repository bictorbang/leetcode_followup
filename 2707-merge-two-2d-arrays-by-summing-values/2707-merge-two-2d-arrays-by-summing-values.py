class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        hm = defaultdict(int)
        res = []

        while (l < len(nums1) and r < len(nums2)):
            if nums1[l][0] < nums2[r][0]:
                hm[nums1[l][0]] += nums1[l][1]
                res.append([nums1[l][0], hm[nums1[l][0]]])
                l += 1
            elif nums2[r][0] < nums1[l][0]:
                hm[nums2[r][0]] += nums2[r][1]
                res.append([nums2[r][0], hm[nums2[r][0]]])
                r += 1
            else:
                res.append([nums1[l][0], nums1[l][1] + nums2[r][1]])
                r += 1
                l += 1
        while l < len(nums1):
            res.append(nums1[l])
            l += 1
        while r < len(nums2):
            res.append(nums2[r])
            r += 1
        return res

