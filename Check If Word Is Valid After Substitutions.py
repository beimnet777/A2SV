class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        comp=['a','b','c']
        for i in s:
            if stack[-3:]==comp:
                stack.pop()
                stack.pop()
                stack.pop()
            stack.append(i)
        return stack==comp
