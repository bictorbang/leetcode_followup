class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if (finalSum%2): return []
        if finalSum < 5: return [finalSum]
        finalSum //= 2

        N = int((-1 + (1 + 8 * finalSum)**(0.5)) / 2)
        result = list(range(2, 2*N+1, 2))
        result[-1] += 2 * (finalSum - N * (N + 1) // 2)
        
        return result