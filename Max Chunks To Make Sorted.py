class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s=[]
        ctr=0
        while ctr<len(arr):
            if len(s)>1:
                if max(s[-2])>min(s[-1]):
                    s[-2].extend(s[-1])
                    s.pop()
                else:
                    s.append([arr[ctr]])
                    ctr+=1
            else:
                s.append([arr[ctr]])
                ctr+=1
        if len(s)>1:
            while len(s)>1 and max(s[-2])>min(s[-1]):
                s[-2].extend(s[-1])
                s.pop()
        return len(s)
