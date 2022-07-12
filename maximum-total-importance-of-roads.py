class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        x=dict()
        for i in range(n):
            x[i]=0
        for i in roads:
            x[i[0]]+=1
            x[i[1]]+=1
        cand=[(i,x[i]) for i in range(n)]
        cand.sort(key=lambda x:x[1])
        ctr=1
        for i in cand:
            x[i[0]]=ctr
            ctr+=1
        ans=0
        for i in roads:
            ans+=x[i[0]]
            ans+=x[i[1]]
        return ans
