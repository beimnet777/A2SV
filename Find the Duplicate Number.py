class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def count(i):
            tot=0
            for j in nums:
                if j<=i:
                    tot+=1
            return tot
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            ctr=count(mid)
            if ctr<=mid:
                l=mid+1
            else:
                r=mid
        return r
