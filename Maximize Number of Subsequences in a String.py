class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        count=0
        ctr=0
        x=dict()
        if pattern[0]==pattern[1]:
            tot =0
            for i in text:
                if i==pattern[0] :
                    tot+=1 
            return int(((tot+1)/2)*(tot))
        for j,i in enumerate(text):
            if i==pattern[0]:
                count+=1
            elif i==pattern[1]:
                ctr+=1
                x[j]=count
        if ctr>count:
            for i in x.keys():
                x[i]+=1
        else:
            x[-1]=count
        return sum(x.values()) 
