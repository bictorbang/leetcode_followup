# 304. Range Sum Query 2D - Immutable
# Given a 2D matrix matrix, handle multiple queries 
# of the following type:
#
# Calculate the sum of the elements of matrix inside 
# the rectangle defined by its upper left corner (row1, col1) 
# and lower right corner (row2, col2).
#
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix)         
# 
# Initializes the object with the integer matrix matrix.
#
# int sumRegion(int row1, int col1, int row2, int col2) 
# 
# Returns the sum of the elements of matrix inside the 
# rectangle defined by its upper left corner (row1, col1) 
# and lower right corner (row2, col2).
#
# You must design an algorithm where sumRegion 
# works on O(1) time complexity. 


from typing import List
from collections import defaultdict


# Date: 25.01.2025
# Runtime: 1423ms
# Memory: 32.18MB
# 
# It's too slow.

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):


        self.m = len(matrix)
        self.n = len(matrix[0]) # We assume matrix exists (not null)

        self.sums = [0]
        total = 0
        for i in range(self.m):
            for j in range(self.n):
                total += matrix[i][j]
                self.sums.append(total)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            res += self.sums[i*self.n + col2 + 1] - self.sums[i*self.n + col1]
        return res











# Very inefficient first approach.

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0]) # We assume matrix exists (not null)
        self.sums = defaultdict(list)
        for i in range(self.m):
            for j in range(self.n):
                elt = matrix[i][j]
                self.sums[(i, j)].append([elt])
                for (k, l) in self.sums:
                    if ((i,j) != (k,l)) and i>=k and j >= l:
                        sum_kl = self.sums[(k, l)]
                        if i == k:
                            sum_kl[0].append(sum([sum_kl[0][-1], elt]))
                            continue
                        if j == l:
                            sum_kl.append([sum([sum_kl[-1][0], elt])])
                        else:
                            print(f"i = {i}, k = {k}, j = {j}, l = {l}")
                            up = [matrix[x][j] for x in range(k, i + 1)]
                            print(f"{up}")
                            sum_kl[-1].append(sum([sum_kl[-1][-1]] + up))
                            #print(f"sums[{k,l}] = {self.sums[(k,l)]}")
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[(row1, col1)][(row2 - row1)][(col2 - col1)]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)