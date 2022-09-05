class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo=dict()
        def  helper(n,i):
            if n ==len(triangle)-1:
                return triangle[n][i]
            elif (n,i) in memo:
                return memo[(n,i)]
            else:
                first=helper(n+1,i)
                second=helper(n+1,i+1)
                memo[(n,i)]=min(first,second)+triangle[n][i]
                return memo[(n,i)]
        return helper(0,0)     
