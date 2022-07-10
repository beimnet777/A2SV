class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo=dict()
        def helper(index):
            if index>len(cost)-1:
                return 0
            elif index in memo:
                return memo[index]
            else:
                first= cost[index]+helper(index+1) if index>=0 else helper(index+1)
                second=cost[index]+helper(index+2) if index>=0 else helper(index+2)
            memo[index]= first if first<second else second
            return memo[index]
        return helper(-1)
