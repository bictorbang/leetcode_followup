class Solution:
    def isHappy(self, n: int) -> bool:
        n_happy = n
        ht = set()
        while n_happy != 1:
            n_happy = sum((int(i)*int(i) for i in str(n_happy)))
            if n_happy in ht:
                return False
            ht.add(n_happy)
        return True

        