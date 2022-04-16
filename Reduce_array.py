from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
       
        half=len(arr)/2
        freq=Counter(arr)
        count=0
        sumx=0
     
        freq=sorted(freq.values())
        while sumx<half:
            sumx+=freq.pop()
            count+=1
        return count
