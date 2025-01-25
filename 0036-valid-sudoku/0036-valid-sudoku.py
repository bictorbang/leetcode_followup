
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