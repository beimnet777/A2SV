class MyCircularDeque:

    def __init__(self, k: int):
        self.queue=[-1]*k
        self.head=0
        self.tail=1
        self.k=k
        

    def insertFront(self, value: int) -> bool:
        if self.queue[self.head]==-1:
           
            self.queue[self.head]=value
            self.head=(self.head-1+self.k)%self.k
            return True
        return False
    def insertLast(self, value: int) -> bool:
        
        if self.queue[self.tail]==-1:
            self.queue[self.tail]=value
            self.tail=(self.tail+1)%self.k
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.queue[(self.head+1+self.k)%self.k]!=-1:
            self.queue[(self.head+1+self.k)%self.k]=-1
            self.head=(self.head+1+self.k)%self.k
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.queue[(self.tail-1)%self.k]!=-1:
            self.queue[(self.tail-1)%self.k]=-1
            self.tail=(self.tail-1)%self.k
            return True
        return False
            
            
    

    def getFront(self) -> int:
        return self.queue[(self.head+1)%self.k]
        

    def getRear(self) -> int:
        return self.queue[(self.tail-1)%self.k]

    def isEmpty(self) -> bool:
        for i in self.queue:
            if i!=-1:
                return False
        return True
    def isFull(self) -> bool:
        for i in self.queue:
            if i==-1:
                return False
        return True
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
