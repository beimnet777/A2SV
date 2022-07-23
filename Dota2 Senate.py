class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        x=deque(senate)
        c=Counter(x)
        d,r=0,0
        while len(x)>0:
            if d>0:
                if x[0]=='R':
                    d+=1
                    x.append(x.popleft())
                else:
                    d-=1
                    c[x.popleft()]-=1
            elif r>0:
                if x[0]=='D':
                    r+=1
                    x.append(x.popleft())
                else:
                    r-=1
                    c[x.popleft()]-=1
            else:
                if x[0]=='R':
                    d+=1
                    x.append(x.popleft())
                else:
                    r+=1
                    x.append(x.popleft())
            if c['D']==0:
                return 'Radiant'
            elif c['R']==0:
                return 'Dire'
