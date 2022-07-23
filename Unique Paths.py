class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo=dict()
        def helper(m,n):
            if m==1 or n==1:
                return 1
            elif (m,n) in memo:
                return memo[(m,n)]
            else:
                memo[(m,n)]= helper(m-1,n)+helper(m,n-1)
                return memo[(m,n)]
        return helper(m,n)
        
