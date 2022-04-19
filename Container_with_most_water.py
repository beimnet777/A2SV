class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area=float("-inf")
        while i<j:
            if height[i]<height[j]:
                short=height[i]
                area=max(area,((j-i)*short))
                i+=1
            else:
                short=height[j]
                area=max(area,((j-i)*short))
                j-=1
                
            
        return area
