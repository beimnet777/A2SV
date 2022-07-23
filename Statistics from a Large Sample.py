class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        def kth(x):
            counter=0
            for j,i in enumerate(count):
                counter+=i
                if counter>=x:
                    return j
            
        mini,maxi,mode=-1,-1,[-1,-1]
        sumx,counter=0,0
        for j,i in enumerate(count):
            counter+=i
            if mini==-1 and i!=0:
                mini=j
            if i!=0:
                maxi=j
            if mode[0]<i:
                mode[0],mode[1]=i,j
            sumx+=(j*i)
        print(counter)
        
        if counter%2==0:
            median=(kth(counter//2)+kth(counter//2+1))/2
        else:
            median=kth(counter//2+1)
        return [mini,maxi,sumx/counter,median,mode[1]]
