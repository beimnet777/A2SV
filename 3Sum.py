class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for j,i in enumerate(nums):
            target=-i
            r=len(nums)-1
            l=j+1
            while l<r:
                if l==j:
                    l+=1
                elif r==j:
                    r-=1
                elif nums[l]+nums[r]==target:
                    ans.add(tuple((nums[l],nums[r],nums[j])))
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
        return list(ans)
