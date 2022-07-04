class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        x=dict()
        ans=[]
        if len(s)<10 :return
        l,r=0,9
        while r<len(s):
            x[s[l:r+1]]=x.get(s[l:r+1],0)+1
            l+=1
            r+=1
        for i in x.keys():
            if x[i]>1:
                ans.append(i)
        return ans       
