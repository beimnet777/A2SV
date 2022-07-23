class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros=0
        ans=0
        first=None
        l,r=0,0
        while r<len(nums):
            if zeros<2:
                if zeros==0 and nums[r]==0:
                    first=r
                zeros+=1 if nums[r]==0 else 0
                r+=1
            else:
                print(r,l)
                ans=max(ans,r-l-2)
                l=first+1
                first=r-1
                zeros-=1
        if zeros<2:
            ans=max(ans,r-l-1)
        elif zeros==2:
            ans=max(ans,r-l-2)
        return ans
