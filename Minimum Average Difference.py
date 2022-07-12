class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ans=-1
        minx=float('inf')
        n=len(nums)
        
        front_prefix=[0]*len(nums)
        back_prefix=[0]*len(nums)
        
        for j,i in enumerate(nums):
            front_prefix[j]=front_prefix[j-1]+i
            back_prefix[-(1+j)]=back_prefix[-(1+j)+1]+nums[-(1+j)]
            
        for j,i in enumerate(nums):
            before=int((front_prefix[j]/(j+1)))
            after=int((back_prefix[j]-i)/(n-(j+1))) if n-(j+1)!=0 else 0
            diff=abs(before -after)
            if minx >diff:
                ans=j
                minx=diff
                
        return ans
