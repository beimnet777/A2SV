class MyCircularQueue:

    def __init__(self, k: int):
        self.front=0
        self.rear=0
        self.arr=[0]*k
        
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.arr[self.rear%len(self.arr)]=value
            self.rear+=1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.arr[self.front%len(self.arr)]=0
            self.front+=1
            return True
        else:
            return False
        

    def Front(self) -> int:
        return self.arr[self.front%len(self.arr)] if not self.isEmpty() else -1
        
        

    def Rear(self) -> int:
        return self.arr[(self.rear-1)%len(self.arr)] if not self.isEmpty() else -1
        

    def isEmpty(self) -> bool:
        if self.rear%len(self.arr)==self.front%len(self.arr) and self.arr[self.rear%len(self.arr)]==0:return True
        else:False
        

    def isFull(self) -> bool:
        if self.rear%len(self.arr)==self.front%len(self.arr) and self.arr[self.rear%len(self.arr)]!=0:return True
        else:False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
