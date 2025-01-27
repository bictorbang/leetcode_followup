class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        s_r = s[::-1]
        i = 0
        while i < mid:
            if s[i] != s_r[i]:
                a = s[i:mid] == s_r[i+1:mid+1]
                b = s[i+1:mid+1] == s_r[i:mid]
                return a or b
            i += 1

        return True