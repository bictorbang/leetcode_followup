class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        if n < 1: return False
        def prime_factors(n):
            i = 2
            factors = set()
            while i * i <= n:
                if n % i:
                    i += 1
                else:
                    n //= i
                    factors.add(i)
            if n > 1:
                factors.add(n)
            return factors
        factors = prime_factors(n)
        return len(factors & {2, 3, 5}) == len(factors)