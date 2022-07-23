class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        x=sorted(deck)
        ans=[0]*len(deck)
        temp=deque([i for i in range(len(deck))])
        ctr=0
        while temp:
            ans[temp[0]]=x[ctr]
            temp.popleft()
            if temp:
                temp.append(temp.popleft())
            ctr+=1
        return ans
            
