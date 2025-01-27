class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        op = {"+": add, "-" : sub, "*" : mul, "/": lambda a, b : int(a/b)}
        for elt in tokens:
            stack.append(elt)
            if elt in op:
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(op[elt](a, b))
        return int(stack.pop())
