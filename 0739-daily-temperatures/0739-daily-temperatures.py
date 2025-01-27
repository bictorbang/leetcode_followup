class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0 for _ in range(n)]
        stack = [0]
        for i in range(1, n):
            pivot = temperatures[i]    
            while (stack and temperatures[stack[-1]] < pivot):
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        stack.clear()
        return answer
