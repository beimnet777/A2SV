class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.lru={}
        self.recent=0
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lru[key]=self.recent
            self.recent+=1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key not in self.cache and len(self.cache)>=self.capacity:
            to_be_removed=min(self.lru,key= self.lru.get)
            self.cache.pop(to_be_removed)
            self.lru.pop(to_be_removed)
        self.cache[key]=value
        self.lru[key]=self.recent
        self.recent+=1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
