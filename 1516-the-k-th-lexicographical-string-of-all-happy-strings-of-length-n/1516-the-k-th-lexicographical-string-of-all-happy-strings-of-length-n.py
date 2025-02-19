class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.idx = 0
        res = []
        def dfs(cur):
            if len(cur) > 1 and cur[-1] == cur[-2]: return
            if self.idx > k: return
            if len(cur) == n: 
                self.idx += 1
                if self.idx == k: 
                    print(cur)
                    return cur
                res.append(cur[:])
                return
            for elt in "abc":
                step = dfs(cur + elt)
                if step:
                    return step
            return
        return dfs("") or ""
        
