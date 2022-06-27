import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.li=nums
        heapq.heapify(self.li)
        self.k=k
        while (len(self.li))>k:
            heapq.heappop(self.li)
    def add(self, val: int) -> int:
        if self.k<=len(self.li):
            if val<self.li[0]:
                pass
            else:
                heapq.heappush(self.li,val)
                heapq.heappop(self.li)
        else:
            heapq.heappush(self.li,val)
            
        return self.li[0]

        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
