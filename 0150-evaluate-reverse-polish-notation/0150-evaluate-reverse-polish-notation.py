class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+": add, "-" : sub, "*" : mul, "/": truediv}
        for elt in tokens:
            stack.append(elt)
            if elt in op:
                stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(int(op[elt](a, b)))
        return int(stack[-1])
