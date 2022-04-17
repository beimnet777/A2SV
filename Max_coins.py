class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        j=len(piles)-2
        sum=0
        while j>=len(piles)//3:
            sum+=piles[j]
            j-=2
        return sum
