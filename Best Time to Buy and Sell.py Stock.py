class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        ans=0
        for i in range(len(prices)-2,-1,-1):
            maxi=max(prices[i+1],maxi)
            ans=max(ans,maxi-prices[i])
        return ans
