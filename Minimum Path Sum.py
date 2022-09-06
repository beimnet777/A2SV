class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo=dict()
        def helper(r,c):
            if r> len(grid)-1 or c >len(grid[0])-1:
                return float("inf")
            if (r,c)==(len(grid)-1,len(grid[0])-1):
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            else:
                right=helper(r,c+1)
                down=helper(r+1,c)
                memo[(r,c)]=min(right,down)+grid[r][c]
                return memo[(r,c)]
        return helper(0,0)              
