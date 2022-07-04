class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x=set()
        l,r=0,0
        while r<len(nums):
            if r-l> k:
                x.remove(nums[l])
                l+=1
            if nums[r] in x:
                return True
            else:
                x.add(nums[r])
                r+=1
        return False
        
