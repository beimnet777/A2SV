class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        tot=capacityA
        totB=capacityB
        l,r=0,len(plants)-1
        ans=0
        while l<r:
            if plants[l]>capacityA:
                ans+=1
                capacityA=tot
            capacityA-=plants[l]
            if plants[r]>capacityB:
                ans+=1
                capacityB=totB
            capacityB-=plants[r]
            l+=1
            r-=1
        if l==r:
            ans+=1 if plants[l]>capacityA and plants[r]>capacityB else 0
        return ans   
