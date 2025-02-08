class Solution:
    def addDigits(self, num: int) -> int:
        d = num
        while d > 9: 
            d = sum((int(i) for i in str(d)))
        return d