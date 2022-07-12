class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans=[]
        for i in matrix:
            ans.extend(i)
            i=[0]
        ans.sort()
        return ans[k-1]
