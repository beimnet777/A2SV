class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types=[]
        l,r=0,0
        ans=-1
        while r<len(fruits):
            if len(types)<2:
                if fruits[r] in types:
                    pass
                else:
                    types.append(fruits[r])
                r+=1
                    
            else:
                if fruits[r] in types:
                    r+=1
                else:
                    if ans< r-l:
                        ans=r-l
                    start=fruits[r-1]
                    pos=r-1
                    while pos>l:
                        if fruits[pos]!=start:
                            break
                        else:
                            pos-=1
                    index=abs(types.index(start)-1)
                    types.pop(index)
                    l=pos+1
                    r-=1
        if ans< r-l:
            ans=r-l
        return ans
