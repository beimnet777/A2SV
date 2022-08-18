class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited=set()
        def neighbour(t,r,c):
            neigh=[]
            direction=[(0,1),(1,0),(0,-1),(-1,0)]
            for i,j in direction:
                if r+i in range(0,len(grid)) and c+j in range(len(grid[0])) and grid[r+i][c+j]<=t and(r+i,c+j) not in visited:
                    neigh.append((r+i,c+j))
                    visited.add((r+i,c+j))
            return neigh
        def bfs(t):
            if grid[0][0]>t:
                return
            stack=[(0,0)]
            visited.add((0,0))
            while stack:
                cur=stack.pop()
                if cur==(len(grid)-1,len(grid)-1):
                    visited.clear()
                    return True
                neigh=neighbour(t,cur[0],cur[1])
                for i in neigh:
                    stack.append(i)
            visited.clear()
            return
        l,r=0,len(grid)*len(grid)
        while l<r:
            mid=(l+r)//2
            if bfs(mid):
                r=mid
            else:
                l=mid+1
        return l
