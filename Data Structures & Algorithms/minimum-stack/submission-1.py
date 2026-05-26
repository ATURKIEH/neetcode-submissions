import numpy as np
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        smallest = float('inf')
        for i in self.stack:
            if i < smallest:
                smallest = i

        return smallest
        
