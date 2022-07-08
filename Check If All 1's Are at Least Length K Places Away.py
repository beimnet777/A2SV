class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        l=0
        while l<len(nums):
            if nums[l]==1:
                for i in range(k):
                    l+=1
                    if l<len(nums) and nums[l]==1:
                        return False
                
            l+=1
        return True 
