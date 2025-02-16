class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(k, target): 
            if target < 0 or k < target: return
            if k == target: return True
            return (partition(k // 10, target - k % 10) or partition(k // 100, target - k % 100) or partition(k // 1000, target - k % 1000))
        total = 1 # 1 is always gonna work for 1 <= n <= 1000
        for i in range(2, n + 1):
            s = i*i
            if partition(s, i):
                total += s
        return total