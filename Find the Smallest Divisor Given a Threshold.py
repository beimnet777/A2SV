class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sum_x(num,n):
            sumx=0
            for i in num:
                sumx+=math.ceil(i/n)
            return sumx
        l,r=1,10**6
        while l<r:
            mid=(l+r)//2
            x=sum_x(nums,mid)
            if x>threshold:
                l=mid+1
            else:
                r=mid
        return l   
