class MinStack:

    def __init__(self):
        self.minstack = []
        self.l = []
        

    def push(self, val: int) -> None:
        self.l.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        last = self.l.pop()
        if last == self.minstack[-1]:
            self.minstack.pop()

        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()