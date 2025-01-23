from typing import List
from collections import Counter, defaultdict
import heapq

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

# 347. Top K Frequent Elements
def topKFrequent(nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 

# 271. Encode and Decode Strings

def encode(strs: List[str]) -> str:
        res = ""
        for elt in strs:
            res+= f"{len(elt)}#{elt}"
        return res
    
def decode(s: str) -> List[str]:
    res = []
    idx = 0
    while idx < len(s):
        idx2 = idx
        while s[idx] != "#":
            idx2 += 1
        count = int(s[idx:idx2])
        idx = idx2 + 1
        idx2 = idx + count
        res.append(s[idx:idx2])      
        idx = idx2     
    return res