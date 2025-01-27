class Solution:
    def generateAll(self, n):
        yield from itertools.product(*(["()"] * 2*(n-1))) 
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        for p in self.generateAll(n):
            stack = [1]
            for elt in p:
                if elt == ")":
                    if not stack:
                        break
                    stack.pop()
                else:
                    stack.append(1)
                    if len(stack) > n:
                        break
            if len(stack) != 1:
                continue
            stack.pop()
            res.append("(" + "".join(p) + ")")
        return res
            


