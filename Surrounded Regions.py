class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited=set()
        r=len(board)
        c=len(board[0])
        for k in range(r):
            for l in range(c):
                if board[k][l]=='O' and (k,l) not in visited:
                    stack=[(k,l)]
                    islands=[]
                    visited.add((k,l))
                    tot=0
                    flag=True
                    while stack:
                        i,j=stack.pop()
                        tot+=1
                        islands.append((i,j))
                        if i==0 or i==r-1 or j==0 or j==c-1:
                            flag=False
                        if i+1 <r and (i+1,j) not in visited and board[i+1][j]=='O':
                            visited.add((i+1,j))
                            stack.append((i+1,j))
                        if i-1 >-1 and (i-1,j) not in visited and board[i-1][j]=='O':
                            visited.add((i-1,j))
                            stack.append((i-1,j))
                        if j+1 <c and (i,j+1) not in visited and board[i][j+1]=='O':
                            visited.add((i,j+1))
                            stack.append((i,j+1))
                        if j-1 >-1 and (i,j-1) not in visited and board[i][j-1]=='O':
                            visited.add((i,j-1))
                            stack.append((i,j-1))
                    if flag:
                        for row,col in islands:
                            board[row][col]='X'
        return 
