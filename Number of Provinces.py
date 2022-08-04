class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        tot=len(isConnected)
        par=[i for i in range(len(isConnected))]
        rank=[1]*len(isConnected)
        def find(n):
            res=n
            while res!=par[res]:
                par[res]=par[par[res]]
                res=par[res]
            return res
        for i in range(len(isConnected)):
            for j in range(i,len(isConnected)):
                
                if isConnected[i][j]==1:
                    par_i,par_j=find(i),find(j)
                    if par_i!=par_j:
                        if rank[i]>rank[j]:
                            par[par_j]=par_i
                            rank[i]+=1
                            tot-=1
                        else:
                            par[par_i]=par_j
                            rank[j]+=1
                            tot-=1
        return tot
