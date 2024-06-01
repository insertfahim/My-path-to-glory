class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        for item in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        result=self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return result
    def peek(self) -> int:
        for item in range(len(self.stack1)-1):
            self.stack2.append(self.stack1.pop())
        result=self.stack1.pop()
        self.stack1.append(result)
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return result

    def empty(self) -> bool:
        if self.stack1:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()