class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited=set()
        def dfs(k,l):
            stack=[(k,l)]
            visited.add((k,l))
            while stack:
                i,j=stack.pop()
                if i+1 <len(grid) and (i+1,j) not in visited and grid[i+1][j]==1:
                    visited.add((i+1,j))
                    stack.append((i+1,j))
                if i-1 >-1 and (i-1,j) not in visited and grid[i-1][j]==1:
                    visited.add((i-1,j))
                    stack.append((i-1,j))
                if j+1 <len(grid[0]) and (i,j+1) not in visited and grid[i][j+1]==1:
                    visited.add((i,j+1))
                    stack.append((i,j+1))
                if j-1 >-1 and (i,j-1) not in visited and grid[i][j-1]==1:
                    visited.add((i,j-1))
                    stack.append((i,j-1))
        r=[0,len(grid)-1]
        c=[0,len(grid[0])-1]
        for k in r:
            for l in range(len(grid[0])):
                if grid[k][l]==1 and (k,l) not in visited:
                    dfs(k,l)
        for k in c:
            for m in range(len(grid)):
                if grid[m][k]==1 and (m,k) not in visited:
                    dfs(m,k)
        tot=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1 and (row,col) not in visited:
                    tot+=1
        return tot                  
