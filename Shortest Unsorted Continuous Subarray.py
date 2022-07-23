class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start,end=-1,-1
        x=sorted(nums)
        for j,i in enumerate(nums):
            if i!=x[j]:
                if start==-1:
                    start=j
                end=j
        return end-start+1 if start!=-1 else 0   
