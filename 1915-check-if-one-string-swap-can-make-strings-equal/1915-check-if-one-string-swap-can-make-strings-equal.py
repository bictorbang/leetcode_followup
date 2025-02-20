class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        cnt = 0
        letters_1, letters_2 = set(), set()
        for i in range(len(s1)):
            if s1[i] != s2[i]: 
                cnt += 1
                letters_1.add(s1[i])
                letters_2.add(s2[i])
        return cnt == 2 and letters_1 == letters_2