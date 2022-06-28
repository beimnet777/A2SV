import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict=dict()
        ans=[]
        for i in nums:
            num_dict[i]=num_dict.get(i,0)+1
        heap_nums=[(-num_dict[i],i) for i in num_dict.keys() ]
        heapq.heapify(heap_nums)
        for i in range(k):
            ans.append(heapq.heappop(heap_nums)[1])
        return ans
