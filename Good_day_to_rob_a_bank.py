class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        i=1
        j=len(security)-1
        prev_front=security[0]
        prev_back=security[j]
        sum1=0
        sum2=0
        before=[0]*len(security)
        after=[0]*len(security)
        ans=[]
        j-=1
        while i<len(security) and j>0:
            if security[i]<= prev_front:
                sum1+=1
            else:
                sum1=0
            prev_front=security[i]
            before[i]=(sum1)
            if security[j]<= prev_back:
                sum2+=1
            else:
                sum2=0
            prev_back=security[j]
            after[j]=(sum2)
            j-=1
            i+=1
        i=0 
        while i<len(security):
            if before[i]>=time and after[i]>=time:
                ans.append(i)
            i+=1
        return ans        
