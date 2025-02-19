class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def dfs(cur):
            if len(cur) > 1 and cur[-1] == cur[-2]: return
            if len(cur) == n: 
                res.append(cur[:])
                return
            for elt in "abc":
                dfs(cur + elt)
        dfs("")
        if k > len(res): return ""
        return res[k - 1]
        
