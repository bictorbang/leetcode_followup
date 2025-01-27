class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile(r"[\W_]+")
        pattern = pattern.sub("", s).upper()
        n = len(pattern)
        if n == 0: return True
        i = 0
        j = n - 1
        while i < j:
            if pattern[i] != pattern[j]: return False
            i+=1
            j-=1
        return True