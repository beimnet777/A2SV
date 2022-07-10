class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=[]
        stack_t=[]
        for i in range(len(s)):
            if s[i]=='#':
                if len(stack_s)>0:stack_s.pop()
            else:stack_s.append(s[i])
        for i in range(len(t)):
            if t[i]=='#':
                if len(stack_t)>0:stack_t.pop()
            else:stack_t.append(t[i])
        return stack_s==stack_t
