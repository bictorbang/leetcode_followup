class Solution:
    def check(self, nums: List[int]) -> bool:

        def get_rotations(n):
            for _ in range(len(n)):
                n.rotate()
                yield n

        perms = get_rotations(deque(sorted(nums)))
        nums = deque(nums)
        for perm in perms:
            print(perm)
            if perm == nums: return True
        return False