class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_max = 2**31
        digits = str(n)
        m = len(digits)
        swap1, swap2 = 0, 0
        for i in range(m - 1, 0, -1):
            if digits[i] > digits[i-1]:
                swap1 = i-1
                for j in range(m-1, i-1, -1):
                    if digits[j] > digits[i-1]:
                        swap2 = j
                        break
                break
        if swap1 == swap2:
            return -1
        res = int(digits[:swap1] + digits[swap2] + (digits[swap1 + 1:swap2] + digits[swap1] + digits[swap2+1:])[::-1])

        return res if res < n_max else -1


