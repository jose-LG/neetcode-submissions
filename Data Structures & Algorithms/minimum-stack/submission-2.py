class MinStack:

    def __init__(self):
        self.stack = []
        self.minElements = []

    def push(self, val: int) -> None:
        #What if we append each value to it's corresponidng position
        #So 
        self.stack.append(val)

        if len(self.minElements) == 0:
            self.minElements.append(val)
        else:
            self.minElements.append(min(self.minElements[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.minElements.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        returnVal = self.minElements[-1]
        return returnVal
        
