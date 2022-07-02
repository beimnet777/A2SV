class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list=path.split("/")
        stack=[]
        for i in path_list:
            if i=="." or i=='':
                pass
            elif i==".." :
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(i)
        path=""
        for i in stack:
            path+=("/"+i)
        return path if len(stack)>0 else "/"
