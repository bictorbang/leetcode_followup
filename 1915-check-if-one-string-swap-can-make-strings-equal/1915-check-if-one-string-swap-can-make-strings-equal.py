class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:      
        if s1 == s2: return True
        cnt = 0
        idx1, idx2 = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]: 
                cnt += 1
                if cnt > 2: return False
                if cnt == 1: idx1 = i
                else: idx2 = i
        return s1[idx1] == s2[idx2] and s1[idx2] == s2[idx1]