from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count=dict(Counter(changed))
        changed.sort()
        keys=set(count.keys())
        org=[]
        i=0
        for i in changed:
            if i==0:
                if count[i]>1:
                    org.append(i)
                    count[i]-=2
            else:
                if count[i]>0:        
                    if i*2 in keys and count[i*2]>0:
                        org.append(i)
                        count[i]-=1
                        count[i*2]-=1
                    elif i/2 in keys and count[i/2]>0:
                        org.append(int(i/2))
                        count[i]-=1
                        count[i/2]-=1
                    else:
                        pass
        if len(org)==len(changed)/2:
            return org
        return []
