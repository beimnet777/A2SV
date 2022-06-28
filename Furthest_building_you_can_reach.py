class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        i=0
        ans=0
        heapq.heapify(heap)
        while i<len(heights)-1:
            if heights[i+1]-heights[i]>0:
                heapq.heappush(heap,heights[i+1]-heights[i])
                if len(heap)>ladders:
                    temp=heapq.heappop(heap)
                    if temp>bricks:
                        ans+=len(heap)
                        return ans
                    else:
                        ans+=1
                        bricks-=temp
            else:
                ans+=1
            i+=1
        return ans+len(heap)        
