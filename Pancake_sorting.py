class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        j=len(arr)
        length=len(arr)
        flips=[]
        for i in range(length):
            
            k=arr.index(j)+1
            
            flips.append(k)
           
            flips.append(j)
            rev=arr[:k]
            
            rev=reversed(rev)
      
            arr[:k]=rev
            rev=arr[:j]
            rev=reversed(rev)
           
            arr[:j]=rev
            j-=1
      
        return flips
            
        
        
