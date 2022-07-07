class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        x=[]
        heapq.heapify(x)
        l=0
        while l<len(trips):
            capacity-=trips[l][0]
            if capacity-trips[l][0]<0:
                while len(x)>0 and capacity<0:
                    j=heapq.heappop(x)
                    if j[0]<=trips[l][1]:
                        capacity+=j[1]
                if capacity<0:
                    return False
            heapq.heappush(x,(trips[l][2],trips[l][0]))
            l+=1
        return True
                      
