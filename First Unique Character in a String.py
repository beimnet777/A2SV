class Solution:
    def firstUniqChar(self, s: str) -> int:
        x=Counter(s)
        for j,i in enumerate(s):
            if x[i]==1:
                return j
        return -1  
