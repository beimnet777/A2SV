class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        ans=float("inf")
        sumx=0
        while r<len(nums):
            if sumx>=target:
                ans=min(ans,r-l)
                sumx-=nums[l]
                l+=1
            else:
                sumx+=nums[r]
                r+=1
            
        if sumx>=target:
            while l<r and sumx>=target :
                sumx-=nums[l]
                l+=1
            ans=min(ans,r-l+1)
        return ans if ans !=float('inf') else 0
