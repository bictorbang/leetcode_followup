class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        if n == 1: return [[s]]

        def is_palindrome(s):
            return s == s[::-1] 
        cur = []
        def bt(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    bt(end, path + [s[start:end]])
        bt(0, [])
        return res
                    



        
        bt(s, 0)
        return []

            