class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        l,m,r=0,1,2
        while r<len(nums):
            if nums[l]==nums[m] and nums[m]==nums[r]:
                nums.remove(nums[r])
            else:
                l+=1
                m+=1
                r+=1
        return len(nums)
