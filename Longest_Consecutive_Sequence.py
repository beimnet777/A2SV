class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        ans=0
        heapq.heapify(nums)
        prev=heapq.heappop(nums)
        ctr=1
        while len(nums)>0:
            x=heapq.heappop(nums)
            if x==prev+1:
                ctr+=1
            elif x==prev:
                pass
            else:
                ans=max(ans,ctr)
                ctr=1
            prev=x
        ans=max(ans,ctr)
        return ans   
