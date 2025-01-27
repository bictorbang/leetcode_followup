class Solution:
    def validPalindrome(self, s: str) -> bool:
        def remove(s, idx):
            if idx == 0:
                return s[1:]
            if idx == len(s) - 1:
                return s[:-1]
            return s[:idx] + s[idx + 1:]

        def valid(s, flag):
            if flag > 1: return False
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1    
                else:
                    return (valid(remove(s, l), flag + 1) or valid(remove(s, r), flag + 1))
            return True

        return valid(s, 0)