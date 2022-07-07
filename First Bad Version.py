# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=1,n
        while l<r-1:
            x=(l+r)//2
            if not isBadVersion(x):
                l=x+1
            else:
                r=x-1
        if isBadVersion(l):
            return l
        elif isBadVersion(r):
            return r
        else:
            return l-1 if isBadVersion(l-1) else r+1  
