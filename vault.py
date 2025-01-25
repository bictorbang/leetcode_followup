from typing import List
from collections import Counter, defaultdict, OrderedDict
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

# 1929. Concatenation of Arrays

def getConcatenation(nums: List[int]) -> List[int]:
        return 2*nums

# 146. LRU Cache

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# 303. Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] # Also changes a (lists are immutable)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.a[right]
        return self.a[right] - self.a[left - 1]

# 304. Range Sum Query 2D - Immutable

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix[0])
        m = len(matrix)
        self.sums = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            rowsum = 0
            for j in range(n): # Assume it exists.
                rowsum += matrix[i][j]
                self.sums[i+1][j+1] = self.sums[i][j+1] + rowsum
   
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]

