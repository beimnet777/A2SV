class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot=sum(nums)
        sumx=0
        for j,i in enumerate(nums):
            prev=sumx
            sumx+=i
            back=tot-sumx
            if prev==back:
                return j
        return -1
