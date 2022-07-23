class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=Counter(nums)
        for i in x.keys():
            if x[i]>(len(nums)/2):
                return i 
