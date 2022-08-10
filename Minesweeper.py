class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def adj(r,c):
            direction=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
            neigbours=[]
            tot=0
            for i,j in direction:
                new_r,new_c=r+i,c+j
                if new_r in range(0,len(board)) and new_c in range(0,len(board[0])) and (new_r,new_c) not in visited:
                    if board[new_r][new_c]=='M':
                        tot+=1
                    elif board[new_r][new_c]=='E':
                        neigbours.append((new_r,new_c))
            return (tot,neigbours) if tot==0 else (tot,[])
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        visited=set()
        stack=[(click[0],click[1])]
        visited.add((click[0],click[1]))
        while stack:
            cur_r,cur_c=stack.pop()
            mines,neigb=adj(cur_r,cur_c)
            if mines==0:
                board[cur_r][cur_c]='B'
                for i,j in neigb:
                    stack.append((i,j))
                    visited.add((i,j))
            else:
                board[cur_r][cur_c]=str(mines)
        return board                  
