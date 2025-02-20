class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cur_longest = 1
        longest = 1
        cur = -1 # -1 at init or if equal, 0 if decreasing, 1 if increasing
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if cur == 1:
                    cur_longest += 1
                else:
                    longest = max(cur_longest, longest)
                    cur = 1
                    cur_longest = 2
            elif nums[i] < nums[i - 1]:
                if cur == 0:
                    cur_longest += 1
                else:
                    longest = max(cur_longest, longest)
                    cur = 0
                    cur_longest = 2
            else:
                longest = max(cur_longest, longest)
                cur = -1
                cur_longest = 1

        return max(cur_longest, longest)