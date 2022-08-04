class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l,r=0,len(i)-1
            while l<=r:
                mid=(l+r)//2
                if i[mid]<target:
                    l=mid+1
                elif i[mid]>target:
                    r=mid-1
                else:
                    return True
        return 
