class FrontMiddleBackQueue:

    def __init__(self):
        self.arr=deque()
        self.arr2=deque()

    def pushFront(self, val: int) -> None:
        self.arr.appendleft(val)
        if len(self.arr)>len(self.arr2)+1:
            self.arr2.appendleft(self.arr.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.arr)==len(self.arr2):
            self.arr.append(val)
        elif len(self.arr)==len(self.arr2)+1:
            self.arr2.appendleft(self.arr.pop())
            self.arr.append(val)

    def pushBack(self, val: int) -> None:
        self.arr2.append(val)
        if len(self.arr2)>len(self.arr):
            self.arr.append(self.arr2.popleft())

    def popFront(self) -> int:
        if len(self.arr)>0 :
            x=self.arr.popleft()
            if len(self.arr2)>len(self.arr):
                self.arr.append(self.arr2.popleft())
            return x
        else:
            return  -1

    def popMiddle(self) -> int:
        if len(self.arr)>0 :
            x=self.arr.pop()
            if len(self.arr2)>len(self.arr):
                self.arr.append(self.arr2.popleft())
            return x
        else:
            return  -1

    def popBack(self) -> int:
        if len(self.arr2)>0 :
            x=self.arr2.pop()
            if len(self.arr)>len(self.arr2)+1:
                self.arr2.appendleft(self.arr.pop())
            return x
        elif len(self.arr)>0:
            return self.arr.pop()
        else:
            return  -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
