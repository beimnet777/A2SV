class Solution:
    def largestInteger(self, num: int) -> int:
        even=[]
        odd=[]
        ans=[]
        while num>0:
            x=num%10
            if x%2==0:
                even.append(x)
                ans.append(1)
            else:
                odd.append(x)
                ans.append(-1)
            num=num//10
        even.sort()
        odd.sort()
        ans=list(reversed(ans))
        for j,i in enumerate(ans):
            if i==-1:
                ans[j]=str(odd.pop())
            else:
                ans[j]=str(even.pop())
        return int("".join(ans))
