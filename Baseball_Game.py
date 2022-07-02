class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in ops:
            if i=="C":
                stack.pop()
            elif i=='+':
                stack.append(stack[-1]+stack[-2])
            elif  i=="D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(i))
        return sum(stack)
