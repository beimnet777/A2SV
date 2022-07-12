class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumx=0
        minx=0
        ans=float('-inf')
        for i in nums:
            sumx+=i
            if sumx<minx:
                ans=max(ans,sumx-minx)
                minx=min(minx,sumx)
                continue
            ans=max(ans,sumx-minx)
        return ans
