# 242. Valid Anagram
# Given two strings s and t, return true if t 
# is an anagram of s, and false otherwise.

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t) # Not efficient. (19ms, 18.51MB)
        return Counter(s) == Counter(t)