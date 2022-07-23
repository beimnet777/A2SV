class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minx=(float('inf'),-1)
        maxx=(float('-inf'),-1)
        for j,i in enumerate(nums):
            if i > maxx[0]:
                maxx=i,j
            if i<minx[0]:
                minx=i,j
        if maxx[1]>minx[1]:
            choice1=maxx[1]+1
            choice2=len(nums)-minx[1]
            choice3=minx[1]+len(nums)-maxx[1]+1 
        else:
            choice1=minx[1]+1
            choice2=len(nums)-maxx[1]
            choice3=maxx[1]+len(nums)-minx[1]+1
        return min(choice1,choice2,choice3)
