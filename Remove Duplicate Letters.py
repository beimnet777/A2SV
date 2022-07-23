class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        x=Counter(s)
        in_stack=set()
        stack=[]
        for i in s:
            if i not in in_stack:
                while stack and stack[-1]>i and x[stack[-1]]>0:
                    in_stack.remove(stack.pop())
                stack.append(i)
                x[i]-=1
                in_stack.add(i)
            else:
                x[i]-=1                
        return "".join(stack) 
