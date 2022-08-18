class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        start=[]
        tot=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==1:
                    tot+=1
                elif grid[i][j]==2:
                    start.append(((i,j),0))
        def neighbour(r,c,grid):
            direction=[(0,1),(0,-1),(1,0),(-1,0)]
            neigh=[]
            for i,j in direction:
                if r+i in range(0,len(grid)) and c+j in range(0,len(grid[0])) and grid[r+i][c+j]==1:
                    neigh.append((r+i,c+j))
                    grid[r+i][c+j]=2
            return neigh
        q=deque(start)
        minute=0
        while q:
            cur,level=q.popleft()
            neigh=neighbour(cur[0],cur[1],grid)
            tot-=len(neigh)
            minute=level
            for i in neigh:
                q.append((i,level+1))
        return minute if tot==0 else -1        
