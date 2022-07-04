class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards)<2: return -1
        ans=float("inf")
        x=set([cards[0]])
        l,r=0,1
        while r<len(cards):
            if cards[r] in x:
                ans=min(ans,r-l+1)
                x.remove(cards[l])
                l+=1
            else:
                x.add(cards[r])
                r+=1
        return ans if ans < float('inf') else -1
