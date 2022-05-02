class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth=0
        l,r=0,1
        while r<len(prices):
            if prices[r-1]-prices[r]==1:
                pass
            else:
                smooth+=self.sumRange(r-l)
                l=r
            r+=1
        smooth+=self.sumRange(r-l)
        return smooth
                
    def sumRange(self,n):
        sumR=0
        for i in range(1,n+1):
            sumR+=i
        return sumR
