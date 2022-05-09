class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        answer=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                increment=nums[i-1]-nums[i]
                nums[i]+=(increment+1)
                answer+=(increment+1)
        return answer
