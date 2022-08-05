class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        x=dict()
        self.leader=[]
        top=[-1,0]
        for i in persons:
            x[i]=x.get(i,0)+1
            if x[i]>=top[1]:
                self.leader.append(i)
                top[0],top[1]=i,x[i]
            else:
                self.leader.append(top[0])
        self.time=times
                

    def q(self, t: int) -> int:
        l,r=0,len(self.time)-1
        while l<r:
            mid=(l+r)//2
            if self.time[mid]>t:
                r=mid-1
            elif self.time[mid]<t:
                l=mid+1
            else:
                l=mid
                break
        if self.time[l]>t and l>0:
            l-=1
        return self.leader[l]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
