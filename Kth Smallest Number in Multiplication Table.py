class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def num_beneath(x):
            ctr=0
            for i in range(1,m+1):
                ctr+= min(n,x//i)
            return ctr
        l,r=0,m*n
        while l<r:
            mid=(l+r)//2
            if num_beneath(mid)>=k:
                r=mid
            else:
                l=mid+1
        return l
