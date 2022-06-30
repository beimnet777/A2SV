class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def helper(i,j):
            if i==j:
                return (nums[i],0)
            if i>j:
                return (0,0)
            x1,y1=helper(i+1,j)
            x2,y2=helper(i,j-1)
           
            return max(y1+nums[i],y2+nums[j]),min(x1,x2)
        b1,b2=helper(0,len(nums)-1)
        return b1>=b2
