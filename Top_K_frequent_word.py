class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict=dict()
        ans=[]
        temp=[]
        for i in words:
            word_dict[i]=word_dict.get(i,0)+1
        word_heap=[(-word_dict[i],i) for i in sorted(word_dict)]
        heapq.heapify(word_heap)
        for i in range(k):
            x=heapq.heappop(word_heap)
            ans.append(x[1])
        temp.sort()
        ans.extend([i[1] for i in temp])
        return ans      
