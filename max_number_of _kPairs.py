class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j=0,len(nums)-1
        count=0
        while i<j:
            if nums[i]+nums[j]==k:
                count+=1
