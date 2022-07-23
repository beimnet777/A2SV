class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        string=list(s)
        stack=[]
        ans=[]
        heapq.heapify(ans)
        for j,i in enumerate(string):
            if i=='(':
                stack.append((j))
            elif i==')':
                if stack:
                    stack.pop()
                else:
                    heapq.heappush(ans,-j)
        while stack:
            heapq.heappush(ans,-stack.pop())
        while ans:
            string.pop(-heapq.heappop(ans))
        return "".join(string)
