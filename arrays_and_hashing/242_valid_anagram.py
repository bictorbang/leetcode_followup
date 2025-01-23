# 242. Valid Anagram
# Given two strings s and t, return true if t 
# is an anagram of s, and false otherwise.

from collections import Counter

# Date: 23.01.2025
# Runtime: 5ms (93.55%)
# Memory: 17.87MB (48.55%)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t) # Not efficient. (19ms, 18.51MB)
        return Counter(s) == Counter(t)