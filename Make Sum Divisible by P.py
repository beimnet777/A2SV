class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        k=p
        ans=float('inf')
        prefix=[0]*len(nums)
        x={0:-1}
        for j,i in enumerate(nums):
            prefix[j]=prefix[j-1]+i
        target=prefix[-1]%k
        if target==0:
            return 0
        for j,i in enumerate(prefix):
            if (i-target)%k in x:
                ans=min(ans,j-x[(i-target)%k])
            x[i%k]=j
        return ans if ans !=float('inf') and ans!=len(nums) else -1 
