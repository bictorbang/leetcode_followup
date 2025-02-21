class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12 or n < 4: return []
        valid_IP = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
        res = []
        def backtrack(s, idx, i):
            m = len(s)
            if i == 3 or idx == m - 1:
                if re.match(valid_IP, s):
                    res.append(s[:])
                return
            for j in range(idx + 2, m + 1):
                backtrack(s[:j-1] + "." + s[j-1:], j, i + 1)
        backtrack(s, 0, 0)
        return res



