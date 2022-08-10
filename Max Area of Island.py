class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        r=len(grid)
        c=len(grid[0])
        ans=0
        for k in range(r):
            for l in range(c):
                if grid[k][l]==1 and (k,l) not in visited:
                    stack=[(k,l)]
                    visited.add((k,l))
                    tot=0
                    while stack:
                        i,j=stack.pop()
                        tot+=1
                        if i+1 <r and (i+1,j) not in visited and grid[i+1][j]==1:
                            visited.add((i+1,j))
                            stack.append((i+1,j))
                        if i-1 >-1 and (i-1,j) not in visited and grid[i-1][j]==1:
                            visited.add((i-1,j))
                            stack.append((i-1,j))
                        if j+1 <c and (i,j+1) not in visited and grid[i][j+1]==1:
                            visited.add((i,j+1))
                            stack.append((i,j+1))
                        if j-1 >-1 and (i,j-1) not in visited and grid[i][j-1]==1:
                            visited.add((i,j-1))
                            stack.append((i,j-1))
                    if tot>ans:
                        ans=tot
        return ans        
