class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n_sq = len(grid)**2
        s_a = sum(sum(x) for x in grid)
        s_e = n_sq*(n_sq + 1) / 2
        s_a_sq = sum(sum(map(lambda x: x ** 2, y)) for y in grid)
        s_e_sq = n_sq * (n_sq + 1) * (2*n_sq + 1) / 6
        b = (s_a_sq - s_e_sq - (s_a - s_e)**2)/(2*(s_a - s_e))
        a = b + s_a - s_e
        return [int(a), int(b)]