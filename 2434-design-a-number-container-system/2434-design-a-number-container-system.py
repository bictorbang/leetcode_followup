class NumberContainers:

    def __init__(self):
        self.containers = {} # keys are container indexes
        self.numbers = defaultdict(list) # keys are numbers
        
    def change(self, index: int, number: int) -> None:
        self.containers[index] = number
        heappush(self.numbers[number], index)

    def find(self, number: int) -> int:
        if number not in self.numbers: return -1
        while self.numbers[number]:
            i = self.numbers[number][0]
            if self.containers[i] == number: return i
            heappop(self.numbers[number])
        return -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)