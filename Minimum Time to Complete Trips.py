class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def get_trips(n):
            tot=0
            for i in time:
                tot+=(n//i)
            return tot
        l,r=1,max(time)*totalTrips
        while l<r:
            mid=(l+r)//2
            
            trip=get_trips(mid)
            if trip<totalTrips:
                l=mid+1
            else:
                r=mid  
        return l   
