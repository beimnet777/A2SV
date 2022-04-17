class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=self.starting)
        i=0
        j=1
        while j<len(intervals):
            if intervals[i][1]>=intervals[j][0] and intervals[i][1]<=intervals[j][1]:
                intervals[i]=[intervals[i][0],intervals[j][1]]
                intervals.pop(j)
            elif intervals[i][1]>=intervals[j][0] and intervals[i][1]>=intervals[j][1]:
                intervals.pop(j)
            else:
                j+=1
                i+=1
                
            
        return intervals
        
    def starting(self,num):
        return num[0]
