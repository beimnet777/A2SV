class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str=[str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if int(num_str[i]+num_str[j])>int(num_str[j]+num_str[i]):
                    (num_str[i]),(num_str[j])=(num_str[j]),(num_str[i])
        ans="".join(num_str)
        if int(ans)==0:
            return "0"   
        return ans
    
    
        
