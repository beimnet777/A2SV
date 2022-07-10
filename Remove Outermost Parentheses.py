class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        x=list(s)
        s=0
        ctr=0
        ans=set()
        r=0
        while r<len(x):
            if x[r]==')':ctr+=1
            else:ctr-=1
            if ctr==0:
                ans.add(s)
                ans.add(r)
                s=r+1
            r+=1
        ans2=[i for j,i in enumerate(x) if j not in ans]
        return "".join(ans2)
