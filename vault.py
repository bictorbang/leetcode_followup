from typing import List

# 217. Contains Duplicate
def containsDuplicate(nums: List[int]):
    return len(set(nums)) < len(nums)

