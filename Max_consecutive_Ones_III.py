class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        ans=0
        zero_index=[]
        while r<len(nums):
            if nums[r]==0:
                zero_index.append(r)
                if len(zero_index)>k:
                    if ans<r-l:
                        ans=r-l
                    l=zero_index.pop(0)+1
                    
            r+=1
        if ans <r-l:
            ans =r-l
        return ans
