class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ans=0
        nums.sort()
        ctr=0
        while ctr<len(nums)-1:
            if nums[ctr+1]-nums[ctr] > ans: 
                ans=nums[ctr+1]-nums[ctr]
            ctr+=1
        return ans 
