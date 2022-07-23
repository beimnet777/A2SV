class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        ans=[-1,-1]
        flag=0
        while l<len(nums):
            if nums[l]==target and flag==0:
                ans[0]=l
                ans[1]=l
                flag=1
            elif nums[l]==target and flag==1:
                print(l)
                ans[1]=(l)
            elif nums[l]>target:
                break
            l+=1
        return ans     
