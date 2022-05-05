class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_dict={0:1}
        i=0
        sumx=0
        ans=0
        while i<len(nums):
            if nums[i]%2!=0:
                sumx+=1
            diff=sumx-k
            if diff in prefix_dict:
                ans+=prefix_dict[diff]
            if sumx in prefix_dict:
                prefix_dict[sumx]+=1
            else:
                prefix_dict[sumx]=1
            i+=1  
        return ans
