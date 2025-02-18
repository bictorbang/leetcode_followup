class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2*n - 1)
        hashmap = set()

        def dfs(idx):
            if len(hashmap) == n: return res
            if (res[idx]): return dfs(idx + 1)

            for x in range(n, 0, -1):
                if (x not in hashmap):
                    sec = idx + x
                    if (x == 1): sec = idx
                    if (sec < len(res) and res[idx] == 0 and res[sec] == 0):
                        res[idx], res[sec] = x, x
                        hashmap.add(x)
                        next_step = dfs(idx + 1)
                        if next_step: return next_step
                        hashmap.remove(x)
                        res[idx], res[sec] = 0, 0
        
        return dfs(0)

