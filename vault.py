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

# 238. Product of Array Except Self

def productExceptSelf(nums: List[int]) -> List[int]:
    output = [1] * len(nums)
    
    product = 1
    for i in range(len(nums)): # prefix
        output[i] *= product
        product *= nums[i]
    
    product = 1
    for i in reversed(range(len(nums))): # suffix
        output[i] *= product
        product *= nums[i]

    return output   

# 36. Valid Sudoku

def isValidSudoku(board: List[List[str]]) -> bool:
    s = [set() for _ in range(9)]
    r = [set() for _ in range(9)]
    c = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            elt = board[i][j]
            if elt == ".":
                continue
            if elt in r[i]:
                return False
            r[i].add(elt)
            if elt in c[j]:
                return False
            c[j].add(elt) 
            k = (i // 3)*3 + j // 3
            if elt in s[k]:
                return False
            s[k].add(elt)
    return True

# 128. Longest Consecutive Sequence

def longestConsecutive(nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums:
                length = 1
                while n + length in nums:
                    length += 1
                longest = max(longest, length)
        return longest