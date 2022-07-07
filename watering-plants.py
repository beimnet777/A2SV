class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        tot=capacity
        ans=0
        for j,i in enumerate(plants):
            if i>tot:
                tot=capacity
                ans+=2*(j)
            tot-=i    
            ans+=1
        return ans
