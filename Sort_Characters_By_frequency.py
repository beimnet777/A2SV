class Solution:
    def frequencySort(self, s: str) -> str:
        li=list(s)
        ans=""
        letters=dict()
        for i in li:
            letters[i]=letters.get(i,0)+1
        letters=dict(sorted(letters.items(),key= lambda x:-x[1]))
        for i in letters.items():
            ans+=(i[0]*i[1])
        return ans      
