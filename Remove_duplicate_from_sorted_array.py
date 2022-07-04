class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        l,r=0,1
        while r<len(nums):
            if nums[l]==nums[r]:
                nums.remove(nums[r])
            else:
                l+=1
                r+=1
        return len(nums)
