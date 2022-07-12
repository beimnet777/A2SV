import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans=[0]*len(spells)
        n=len(potions)
        potions.sort()
        for j,i in enumerate(spells):
            l=0
            r=n
            target=math.ceil(success/i)
            while l<r:
                mid=l+(r-l)//2
                if potions[mid]>=target:
                    r=mid
                else:
                    l=mid+1
            ans[j]=n-l
        return ans
