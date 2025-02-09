class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        true_len = len(nums1) - len(nums2)

        for x in nums2:
            while nums1[i]<x and i < true_len:
                i += 1
            if i < true_len:
                for j in range(len(nums1)-1, i, -1):
                    nums1[j] = nums1[j-1]
            nums1[i] = x
            true_len += 1  