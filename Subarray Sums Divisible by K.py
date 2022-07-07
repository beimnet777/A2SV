class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans=0
        x={0:1}
        prefix=[0]*len(nums)
        for j,i in enumerate(nums):
            prefix[j]=prefix[j-1]+i
        for i in prefix:
            if i%k in x:
                ans+=x.get((i%k),0)
            x[i%k]=x.get(i%k,0)+1
        return ans
