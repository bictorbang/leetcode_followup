# 49. Group Anagrams
# Given an array of strings strs, group the anagrams
# together. You can return the answer in any order.

from typing import List
from collections import defaultdict

# Date: 23.01.2025
# Runtime: 11ms (83.37%) 
# Memory: 20.59MB (74.80%)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(List)

        for s in strs:
            sorted_s = "".join(sorted(s))
            anagrams[sorted_s].append(s)
        
        return list(anagrams.values())
