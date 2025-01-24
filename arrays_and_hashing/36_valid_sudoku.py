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
# Runtime: 5ms (51.25%)
# Memory: 17.70MB (63.35%)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_subboard = defaultdict(list)
        hash_row = defaultdict(list)
        hash_col = defaultdict(list)
        for i in range(9):
            for j in range(9):
                elt = board[i][j]
                if elt == ".":
                    continue
            
                if elt in hash_row[i]:
                    return False
                hash_row[i].append(elt)

                if elt in hash_col[j]:
                    return False
                hash_col[j].append(elt)
                
                subboard_idx = (i // 3)*3 + j // 3

                if elt in hash_subboard[subboard_idx]:
                    return False
                hash_subboard[subboard_idx].append(elt)
        return True

# Date: 24.01.2025
# Runtime: 0ms (100%)
# Memory: 17.79MB (47.64%)
# Optimised as much as possible the previous function.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = [set() for _ in range(9)]
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                elt = board[i][j]
                if elt == ".":
                    continue
                if elt in r[i]:
                    return False
                r[i].add(elt)
                if elt in c[j]:
                    return False
                c[j].add(elt) 
                k = (i // 3)*3 + j // 3
                if elt in s[k]:
                    return False
                s[k].add(elt)
        return True