class ProductOfNumbers:

    def __init__(self):
        self.q=deque()
    def add(self, num: int) -> None:
        if len(self.q)>0 and num!=0:
            self.q.appendleft(num*self.q[0])
        elif num==0:
            self.q.clear()
        else:
            self.q.appendleft(num)      
    def getProduct(self, k: int) -> int:
        if k>len(self.q) :return 0
        return self.q[0] if len(self.q)==k else self.q[0]//self.q[k]
