class Solution:
    def rob(self, nums: List[int]) -> int:
        memo=dict()
        def helper(n,x):
            if n >=x:
                return 0
            elif n in memo:
                return memo[n]
            else:
                rob=nums[n%len(nums)]+helper(n+2,x)
                rob_not=helper(n+1,x)
                memo[n]=max(rob,rob_not)
                return memo[n]
        a=helper(0,len(nums)-1)
        memo.clear()
        b=helper(1,len(nums))
        return max(a,b) if len(nums)>1 else nums[0]
