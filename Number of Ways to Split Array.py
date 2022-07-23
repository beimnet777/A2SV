class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        for j,i in enumerate(nums):
            prefix[j]=prefix[j-1]+i
        ans=0
        tot=prefix[-1]
        ctr=0
        while ctr<len(nums)-1:
            if prefix[ctr]>=tot-prefix[ctr]:
                ans+=1
            ctr+=1
        return ans
