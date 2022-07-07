class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans=[]
        x=sum(nums)
        prefix=[0]*len(nums)
        for j,i in enumerate(nums):
            prefix[j]=prefix[j-1]+i   
        for j,i in enumerate(nums):
            left=i*j-(prefix[j-1]) if j>0 else 0
            right=(prefix[len(nums)-1]-prefix[j])-i*(len(nums)-1-j) if j<len(nums)-1 else 0
            result=left+right
            ans.append(result)
        return ans
