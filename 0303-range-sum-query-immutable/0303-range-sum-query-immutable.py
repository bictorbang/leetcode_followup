class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] # Also changes a (lists are immutable)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.a[right]
        return self.a[right] - self.a[left - 1]
