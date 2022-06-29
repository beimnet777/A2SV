from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq=deque()
        def add(num):
            while dq and dq[-1]<num:
                dq.pop()
            dq.append(num)
        def remove(num):
            if num==dq[0]:
                dq.popleft()
            
        dp=[float("-inf")]*len(nums)
        dp[-1]=nums[-1]
        add(nums[-1])
        ctr=1
        for i in range(len(nums)-2,-1,-1):
            dp[i]=dq[0]+nums[i]
            add(dp[i])
            ctr+=1
            if ctr>k:
                remove(dp[i+k])
        return dp[0]          
