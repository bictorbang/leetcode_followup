from functools import cache
class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache
        def partition_dfs(k, pre_sum, target): 
            if not k or found: return
            if int(k) + pre_sum == target: 
                found.append(True)
                total.add(target*target)
                return
            for i in range(1, len(k)):
                partition_dfs(k[i:], pre_sum + int(k[ :i]), target)
        total = {1} # 1 is always gonna work for 1 <= n <= 1000
        for i in range(2, n + 1):
            s = str(i*i)
            found = []
            partition_dfs(s, 0, i)
        return sum(total)