# 36. Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according 
# to the following rules:
#
#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain 
# the digits 1-9 without repetition.
#
# Note:
#
# A Sudoku board (partially filled) could be valid but 
# is not necessarily solvable.
# Only the filled cells need to be validated according 
# to the mentioned rules.

from typing import List
from collections import defaultdict
  

# Date: 24.01.2025
# Runtime: 7ms (40.07%)
# Memory: 17.84MB (29.91%)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_subboard = defaultdict(list)
        hash_row = defaultdict(list)
        hash_col = defaultdict(list)
        for i in range(9):
            for j in range(9):
                elt = board[i][j]
                subboard_idx = f"{i-i%3}{j-j%3}"
                if elt != ".":
                    if elt in hash_row[i] or \
                    elt in hash_col[j] or elt in hash_subboard[subboard_idx]:
                        return False
                    hash_row[i].append(elt)
                    hash_col[j].append(elt)
                    hash_subboard[subboard_idx].append(elt)
        return True

                