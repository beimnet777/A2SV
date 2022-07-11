class Solution:
    def countCollisions(self, directions: str) -> int:
        ans=0
        stack=[directions[0]]
        ctr=1
        while ctr<len(directions):
            if directions[ctr]=='R':
                stack.append(directions[ctr])
            elif directions[ctr]=='L':
                if stack[-1]=='S':
                    ans+=1
                elif stack[-1]=='R':
                    ans+=2
                    stack[-1]='S'
            else:
                stack.append(directions[ctr])
            while len(stack)>1 and stack[-1]=='S' and stack[-2]=='R':
                ans+=1
                stack[-2]='S'
                stack.pop()
            ctr+=1
        return ans
