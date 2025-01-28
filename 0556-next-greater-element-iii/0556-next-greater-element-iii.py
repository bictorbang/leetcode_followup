class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_max = 2**31
        s = str(n)
        for i in range(len(s) - 2, -1, -1):
            if s[i] < s[i + 1]:
                for k in range(len(s) - 1, i, -1):
                    if s[i] < s[k]:
                        res = int(s[:i] + s[k] + s[-1:k:-1] + s[i] + s[k-1:i:-1])
                        return res if res < n_max else -1
        return -1

