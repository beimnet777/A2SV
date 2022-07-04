class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ans=0
        while (a>0 and b>0) or (b>0 and c>0) or (a>0 and c>0):
            if a==min(a,b,c):
                b-=1
                c-=1
            elif b==min(a,b,c):
                a-=1
                c-=1
            else:
                a-=1
                b-=1
            ans+=1
        return ans
