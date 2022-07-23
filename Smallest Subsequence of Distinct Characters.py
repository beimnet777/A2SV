class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ans=[]
        ctr=Counter(s)
        dis=set()
        for i in s:
            if i not in dis:
                while ans and ans[-1]>i and ctr[ans[-1]]>0:
                    x=ans.pop()
                    dis.remove(x)
                ans.append(i)
                dis.add(i)
            ctr[i]-=1
        return "".join(ans)
