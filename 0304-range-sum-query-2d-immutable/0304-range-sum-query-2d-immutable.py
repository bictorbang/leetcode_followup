class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix[0])
        m = len(matrix)
        self.sums = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            rowsum = 0
            for j in range(n): # Assume it exists.
                rowsum += matrix[i][j]
                self.sums[i+1][j+1] = self.sums[i][j+1] + rowsum

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] - self.sums[row2+1][col1] + self.sums[row1][col1]

