class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result=[]
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            result.append(nums[j])
            result.append(nums[i])
            i+=1
            j-=1
        if len(nums)%2!=0:
            result.append(nums[j])
        return result
            
     
        
        
