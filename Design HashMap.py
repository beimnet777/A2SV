class MyHashMap:

    def __init__(self):
        self.x=[[]] *2957
        self.size=2957

    def put(self, key: int, value: int) -> None:
        j=self.hash(key)
        for i in self.x[j]:
            if key==i[0]:
                i[1]=value 
                return
        self.x[j].append([key,value])
        

    def get(self, key: int) -> int:
        j=self.hash(key)
        for i in self.x[j]:
            if key==i[0]:
                return i[1]
        return -1
        

    def remove(self, key: int) -> None:
        k=self.hash(key)
        for j,i in enumerate(self.x[k]):
            if key==i[0]:
                self.x[k].pop(j) 
                return
        return
        
    def hash(self,key)->int:
        return key%2957
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
