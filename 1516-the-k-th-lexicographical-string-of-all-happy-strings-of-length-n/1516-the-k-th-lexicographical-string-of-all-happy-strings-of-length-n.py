class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.idx = 0
        def dfs(cur):
            if self.idx > k: return
            if len(cur) > 1 and cur[-1] == cur[-2]: return
            if len(cur) == n: 
                self.idx += 1
                if self.idx == k: 
                    return cur
                return
            for elt in "abc":
                step = dfs(cur + elt)
                if step:
                    return step
            return
        return dfs("") or ""
        
