class MyQueue:

    def __init__(self):
        self.stack=[]
    def push(self, x: int) -> None:
        self.stack.append(x)
    def pop(self) -> int:
        return self.stack.pop(0)  
    def peek(self) -> int:
        return self.stack[0]  
    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        return False
