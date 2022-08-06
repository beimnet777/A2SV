class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=-1
        ptr=0
        while ptr<len(nums)-1:
            if nums[ptr]>nums[ptr+1]:
                start=ptr
                break
            ptr+=1
        def get(n,start):
            index=(start+n+1)%len(nums)
            return nums[index]
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            num=get(mid,start)
            if num<target:
                l=mid+1
            elif num>target:
                r=mid-1
            else:
                return (start+mid+1)%len(nums)
        return -1
