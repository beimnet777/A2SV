class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(cap,days)-> bool:
            ptr=0
            for i in range(days):
                sumx=0
                while sumx<=cap and ptr<len(weights):
                    sumx+=weights[ptr] 
                    ptr+=1
                if sumx>cap:
                    ptr-=1
                if ptr==len(weights):
                    break
            return ptr==len(weights)
        l,r=1,25*(10**6)
        while l<r:
            mid=(l+r)//2
            if possible(mid,days):
                r=mid
            else:
                l=mid+1
        return  l
