class MyQueue:

    def __init__(self):
        self.stack=[]
        self.temp=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.temp.append(self.stack.pop())
        x=self.stack.pop()  
        for i in range(len(self.temp)):
            self.stack.append(self.temp.pop())
        return x 
    def peek(self) -> int:
        return self.stack[0]  
    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
