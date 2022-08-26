class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        points=list(reversed(points))
        ans=0
        while len(points)>0:
            ans+=1
            start,end=points.pop()
            while len(points)>0 and points[-1][0]<=end:
                temp=points.pop()
                end=min(temp[1],end)
        return ans        
