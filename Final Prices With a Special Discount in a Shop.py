class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[0]*len(prices)
        mono=[]
        for j,i in enumerate(prices):
            if len(mono)>0 and i<=mono[-1][0]:
                while len(mono)>0 and i<=mono[-1][0] :
                    x= mono.pop()
                    ans[x[1]]=x[0]-i
            mono.append((i,j))
        for i in mono:
            ans[i[1]]=i[0]
        return ans
