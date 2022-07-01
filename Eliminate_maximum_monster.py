class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans=1
        time=[]
        for i,j in enumerate(dist):
            time.append(j/speed[i])
        time.sort()
        def key1(elem):
            return elem[0]/elem[1]
        dist.sort()
        ctr=0
        time_min=0
        while ctr<len(time)-1:
            time[ctr+1]-=time_min
            if time [ctr+1]>1:
                ans+=1
            else:
                break
            ctr+=1
            time_min+=1
        return ans        
