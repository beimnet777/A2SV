class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        ans=len(nums)
        l,r=0,ans-1
        while l<=r:
            if nums[l]==val and nums[r]==val:
                return ans -(r-l+1)
            elif nums[l]==val:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                ans-=1
                r-=1
            else:
                l+=1
        return ans
