class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=[" "]* len(score)
        x=[]
        heapq.heapify(x)
        for i,j in enumerate(score):
            heapq.heappush(x,(-j,i))
        ctr=1
        while len(x)>0:
            i,j=heapq.heappop(x)
            if ctr==1:
                ans[j]="Gold Medal"
            elif ctr==2:
                ans[j]="Silver Medal"
            elif ctr==3:
                ans[j]="Bronze Medal"
            else:
                ans[j]=str(ctr)
            ctr+=1
        return ans 
