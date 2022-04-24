class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict={0:1}
        pre_sum=0
        ans=0
        for i in nums:
            pre_sum+=i
            diff=pre_sum-k
            if diff in prefix_dict.keys():
                print("j")
                ans+=prefix_dict[diff]
            if pre_sum in prefix_dict.keys():
                print("k")
                prefix_dict[pre_sum]+=1
            else:
                print("a")
                prefix_dict[pre_sum]=1
        return ans
        
