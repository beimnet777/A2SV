class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,e=0,0
        ans=0
        while e<len(nums):
            while e<len(nums) and (nums[e]-nums[l]<=k):
                e+=1
            ans+=1
            l=e
            e=e
        return ans
