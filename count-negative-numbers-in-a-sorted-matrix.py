class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        tot=0
        for i in grid:
            l,r=0,len(i)-1
            while l<r:
                mid=(l+r)//2
                if i[mid]>=0:
                    l=mid+1
                else:
                    r=mid
            if i[l]<0:
                tot+=len(i)-l
        return tot         
