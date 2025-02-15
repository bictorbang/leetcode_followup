from functools import cache 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        @cache
        def dfs(o, c, s):
                if o == c and o + c == 2*n:
                    res.append(s)
                    return

                if o < n:
                    dfs(o + 1, c, s + "(")
                if c < o:
                    dfs(o, c + 1, s + ")")
        dfs(0, 0, "")

        return res