class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans=0
        x=dict()
        prefix=[0]*len(nums)
        for i,j in enumerate(nums):
            prefix[i]=prefix[i-1]+j if j==1 else prefix[i-1]-1
        for j,i in enumerate(prefix):
            if i in x:
                ans=max(ans,j-x[i])
            elif i==0:
                ans=max(ans,j+1)
            else:
                x[i]=j
        return ans  
