class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans=0
        x=deque()
        for j,i in enumerate(tickets):
            x.append([i,j])
        while True:
            a=x.popleft()
            a[0]-=1
            ans+=1
            if a[0]==0:
                if a[1]==k:
                    return ans
            else:
                x.append(a)
