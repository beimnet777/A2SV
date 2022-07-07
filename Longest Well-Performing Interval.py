class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        x=dict()
        ans=0
        prefix=[0]* len(hours)
        for j,i in enumerate(hours):
            prefix[j]=prefix[j-1]+1 if i>8 else prefix[j-1]-1
        for j,i in enumerate(prefix):
            if i>0:
                ans=max(ans,j+1)
            elif i-1 in x:
                ans=max(ans,j-x[i-1])
            elif i not in x:
                x[i]=j
        return ans 
