class Solution:
    #-1 to sell 0 to buy 1 to cool down -2 to freedom
    def maxProfit(self, prices: List[int]) -> int:
        memo=dict()
        def helper(n,stat):
            if n>len(prices)-1:
                return 0
            elif (n,stat) in memo:
                return memo[(n,stat)]
            else:
                if stat==0:
                    buy=-prices[n]+helper(n+1,1)
                    buy_not=helper(n+1,0)
                    memo[(n,stat)]=max(buy,buy_not)
                elif stat==1:
                    sell=prices[n]+helper(n+2,0)
                    sell_not=helper(n+1,1)
                    memo[(n,stat)]=max(sell,sell_not)
                return memo[(n,stat)]
        return helper(0,0)
