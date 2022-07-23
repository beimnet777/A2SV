class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]==target:
                if nums[l]==target and nums[r]==target:
                    ans.append(l)
                    l+=1
                elif nums[l]==target:
                    r-=1
                else:
                    l+=1
            else:
                r=mid-1
        if nums[l]==target:
            while l<len(nums) and nums[l]==target:
                ans.append(l)
                l+=1
        return ans
