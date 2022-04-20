class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list1=[i for i in range(1,n+1)]
        i=0
        while len(list1)>1:
            for j in range(k-1):
                i+=1
                if i==len(list1):
                    i=0
            list1.remove(list1[i])
            if i==len(list1):
                    i=0
        return list1[0]      
