class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        ans=0
        total_sum=0
        l=r=0
        nums.sort()
        while r<len(nums):
            total_sum+=nums[r]
            if (r-l+1)*nums[r] >total_sum+k:
                total_sum-=nums[l]
                if ans<r-l:
                    ans=r-l
                l+=1
            r+=1
        if ans<r-l:
            ans=r-l
        return ans
