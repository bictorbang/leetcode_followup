class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == "0": return -1
        self.found = False
        powers_of_5 = [str(bin(5**x))[2:] for x in range(6, -1, -1)]
        cur = ""
        def dfs(cur, idx):
            if self.found: return
            if len(cur) > len(s): return
            if cur == s:
                self.found = idx
                return self.found
            for elt in powers_of_5:
                step = dfs(cur + elt, idx + 1)
                if step:
                    return step
            return      
        return dfs(cur, 0) or -1
