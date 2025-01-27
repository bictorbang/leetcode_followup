class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n  # Initialize the result array with -1
        stack = []      # Monotonic stack to track next greater elements
        
        # Iterate through the array twice to simulate circularity
        for i in range(2 * n - 1, -1, -1):
            num = nums[i % n]  # Current element (handle circular index)
            
            # Remove elements from the stack that are <= the current element
            while stack and stack[-1] <= num:
                stack.pop()
            
            # If the stack is not empty, the top of the stack is the next greater element
            if stack:
                res[i % n] = stack[-1]
            
            # Push the current element onto the stack
            stack.append(num)
        
        return res