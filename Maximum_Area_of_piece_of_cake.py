class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        diff1=[horizontalCuts[0],h-horizontalCuts[-1]]
        diff=[verticalCuts[0],w-verticalCuts[-1]]
        i=0
        while i<len(verticalCuts)-1:
            diff.append(verticalCuts[i+1]-verticalCuts[i])
            i+=1
        i=0
        while i<len(horizontalCuts)-1:
            diff1.append(horizontalCuts[i+1]-horizontalCuts[i])
            i+=1
        return max(diff1)*max(diff)%(10**9+7)   
