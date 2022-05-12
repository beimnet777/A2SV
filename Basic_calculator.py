class Solution:
    def calculate(self, s: str) -> int:
        ops=s.split()
        s=''.join(ops)
        stack=[]        
        ans=0
        num1=''
        for i in s:
            if i.isdigit():
                num1+=i
            else:
                stack.append(int(num1))
                break
        if not stack:
            stack.append(int(num1))
        i=0
        while i<len(s):         
            if s[i].isdigit():
                i+=1
            else:
                num2=''
                op=i
                i+=1
                while i<len(s):
                    if s[i].isdigit():
                        num2+=s[i]
                        i+=1
                    else:
                        break
                if s[op]=='-':
                    stack.append(-int(num2))   
                elif s[op]=='*':
                    stack.append(stack.pop()*int(num2))
                elif s[op]=='/':
                    stack.append(int(stack.pop()/int(num2)))
                else:
                    stack.append(int(num2))
        while stack:
            ans+=stack.pop()
        return ans
