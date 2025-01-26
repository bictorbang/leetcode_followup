class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        opens = []
        closes = []

        close_map = {")": "(", "}" : "{", "]" : "["}
        for c in s:
            if c in close_map:
                closes.append(c)
                if not opens:
                    return False
                if opens[-1] == close_map[c]:
                    closes.pop()
                    opens.pop()
                else: return False
            else: opens.append(c)
        
        return len(opens) == 0 and len(closes) == 0

                
