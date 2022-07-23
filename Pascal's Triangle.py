class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[[1]]
        def helper(arr,n):
            if n==1:
                return
            elif n==2:
                arr.append([1,1])
            
            else:
                x=[0]*n
                x[0],x[-1]=1,1
                helper(arr,n-1)
                ctr=1
                ctr2=0
                while ctr2<len(arr[-1])-1 :
                    x[ctr]=arr[-1][ctr2]+arr[-1][ctr2+1]
                    ctr2+=1
                    ctr+=1
                arr.append(x)
        helper(arr,numRows)
        print(arr)
        return arr
