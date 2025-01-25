
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        s = [set() for _ in range(N)]
        r = [set() for _ in range(N)]
        c = [set() for _ in range(N)]
        for i in range(N):
            for j in range(N):
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