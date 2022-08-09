class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        c=len(image[0])
        r=len(image)
        start=image[sr][sc]
        stack=[(sr,sc)]
        visited=set()
        visited.add((sr,sc))
        while stack:
            cur=stack.pop()
            if cur[1]+1<c and (cur[0],cur[1]+1) not in visited and image[cur[0]][cur[1]+1]==start:
                stack.append((cur[0],cur[1]+1))
                visited.add((cur[0],cur[1]+1))
            if cur[1]-1>-1 and (cur[0],cur[1]-1) not in visited and image[cur[0]][cur[1]-1]==start:
                stack.append((cur[0],cur[1]-1))
                visited.add((cur[0],cur[1]-1))
            if cur[0]+1<r and (cur[0]+1,cur[1]) not in visited and image[cur[0]+1][cur[1]]==start:
                stack.append((cur[0]+1,cur[1]))
                visited.add((cur[0]+1,cur[1]))
            if cur[0]-1>-1 and (cur[0]-1,cur[1]) not in visited and image[cur[0]-1][cur[1]]==start:
                stack.append((cur[0]-1,cur[1]))
                visited.add((cur[0]-1,cur[1]))
            image[cur[0]][cur[1]]=color
        return image
