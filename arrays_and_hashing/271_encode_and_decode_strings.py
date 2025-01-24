# 271. Encode and Decode Strings
# Design an algorithm to encode a list of strings 
# to a single string. The encoded string is then decoded 
# back to the original list of strings.
#
# Please implement encode and decode

from typing import List

# Date: 23.01.2025

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for elt in strs:
            res+= f"{len(elt)}#{elt}"
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            count = ""
            while s[idx] != "#":
                count += s[idx]
                idx += 1
            count = int(count)
            res.append(s[idx+1:idx+1+count])      
            idx+= count + 1      
        return res
    
    # More optimised ? Don't have access to the scores (not premium :/)

    def decode(self, s: str) -> List[str]:
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
