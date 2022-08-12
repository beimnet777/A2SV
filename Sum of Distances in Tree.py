class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        for i,j in edges:
            g[i].append(j)
            g[j].append(i)
        nodes=[1]*n
        root_dist=[0]
        ans=[0]*n
        visited=set()
        def dfs(node,depth):
            under=1
            visited.add(node)
            for i in g[node]:
                if i not in visited:
                    under+=dfs(i,depth+1)
                    root_dist[0]+=(depth+1)
            nodes[node]=under
            return under
        dfs(0,0)
        stack=[(0,root_dist[0])]
        visited.clear()
        while stack:
            cur,dist=stack.pop()
            visited.add(cur)
            ans[cur]=dist
            for i in g[cur]:
                if i not in visited:
                    stack.append((i,(dist+n-nodes[i]-nodes[i])))
        return ans            
