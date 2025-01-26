class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        close_map = {")": "(", "}" : "{", "]" : "["}
        for c in s:
            if c in close_map:
                if not stack or stack[-1] != close_map[c]:
                    return False
                else:
                    stack.pop()
            else: stack.append(c)
        
        return not stack

                
