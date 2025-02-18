class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, s = [], []
        n = len(candidates)
        def dfs(idx, s, total):
            if total == target:
                res.append(s[:])
                return
            if total > target or idx >= n: return
            s.append(candidates[idx])
            dfs(idx, s, total + candidates[idx])
            s.pop()
            dfs(idx + 1, s, total)
            return res
        return dfs(0, s, 0)