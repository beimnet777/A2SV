from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frquent=[]
        count=Counter(nums).most_common(k)
        for i,j in count:
            frquent.append(i)
        return frquent
        
        
