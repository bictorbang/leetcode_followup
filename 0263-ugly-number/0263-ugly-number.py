class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        if n < 1: return False
        def prime_factors(n):
            if n % 2 == 0:
                yield 2
                while n % 2 == 0:
                    n = n // 2
            i = 3
            while i * i <= n:
                if n % i == 0:
                    yield i
                    while n % i == 0:
                        n = n // i
                i += 2
            if n > 2:
                yield n
        for prime in prime_factors(n):
            if prime > 5: return False
        return True