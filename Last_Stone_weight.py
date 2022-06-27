import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if (y-x)>0:
                heapq.heappush(stones,x-y)
        return 0 if len(stones)<1 else -stones[0]
