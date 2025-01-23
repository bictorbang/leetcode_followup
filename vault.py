from typing import List
from collections import Counter, defaultdict

# 217. Contains Duplicate
def containsDuplicate(nums: List[int]):
    return len(set(nums)) < len(nums)

# 242. Valid Anagram
def isAnagram(s: str, t: str):
    return Counter(s) == Counter(t)

# 1. Two Sum
def twoSum(nums: List[int], target: int) -> List[int]:
        idx = {}
        for i in range(len(nums)):
            t_ni = target - nums[i]
            if t_ni not in idx:
                idx[nums[i]] = i
            else:
                return (i, idx[t_ni])

# 49. Group Anagrams
def groupAnagrams(strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(List)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)        
        return list(anagrams.values())
