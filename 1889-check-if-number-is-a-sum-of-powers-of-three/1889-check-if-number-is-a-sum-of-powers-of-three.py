class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return digits[::-1]
        return 2 not in numberToBase(n, 3)