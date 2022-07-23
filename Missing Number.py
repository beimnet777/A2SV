class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot=sum(nums)
        tot2=(len(nums)+1)*(len(nums)/2)
        return int(tot2-tot)
