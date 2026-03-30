class MinStack:

    def __init__(self):
        self.stack: List[(int, int)] = []
        

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1] if self.stack else val)))

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        value, _ = self.stack[-1]
        return value
        

    def getMin(self) -> int:
        _, currentMin = self.stack[-1]
        return currentMin
