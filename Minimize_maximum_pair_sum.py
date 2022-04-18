class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        ans=float("-inf")
        while j>i:
            ans=max(ans,nums[i]+nums[j])
            i+=1
            j-=1
        return ans
        
