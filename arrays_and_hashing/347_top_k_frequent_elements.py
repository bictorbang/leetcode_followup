# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, 
# return the k most frequent elements. 
# You may return the answer in any order.

from typing import List
from collections import Counter
import heapq

# Date: 23.01.2025
# Runtime: 4ms (71.54%)
# Memory: 21.30MB (47.79%)
# One liner, that uses a built-in function.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [elt[0] for elt in Counter(nums).most_common(k)]

# Date: 23.01.2025
# Runtime: 2ms (93.96%)
# Memory: 21.31MB (35.37%)
# Gain a little bit more speed at the expense of memory...
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [elt for elt, _ in Counter(nums).most_common(k)]
    

# Runtime: 0ms (100%)
# Memory: 21.37MB (35.37%)
# Using heapq (not my solution)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 