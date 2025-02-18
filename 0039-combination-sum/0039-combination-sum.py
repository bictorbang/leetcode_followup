class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        hashmap = []
        def dfs(s, target):
            if s is not None:
                if sum(s) > target: return
                if sum(s) == target:
                    if sorted(s) not in hashmap:
                        hashmap.append(sorted(s))
                        res.append(s)
                    return
            for elt in candidates:
                s2 = s[:] if s is not None else []
                s2.append(elt)
                dfs(s2, target)
        dfs([], target)
        return res

