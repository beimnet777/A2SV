class Solution:
    #0 for rob and 1 for can't rob
    def rob(self, nums: List[int]) -> int:
        memo=dict()
        def helper(n,stat):
            if n >len(nums)-1:
                return 0
            elif (n,stat) in memo:
                return memo[(n,stat)]
            else:
                if stat==0:
                    rob=nums[n]+helper(n+1,1)
                    rob_not=helper(n+1,0)
                    memo[(n,stat)]=max(rob,rob_not)
                else:
                    memo[(n,stat)]=helper(n+1,0)
                return memo[(n,stat)]
        return helper(0,0)        
