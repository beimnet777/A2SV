class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1=0
        sum2=sum(nums[1:])
        index=0
        while(index<len(nums)-1):
            if sum1==sum2:
                return index
            sum1+=nums[index]
            sum2-=nums[index+1]
            index+=1
        if sum(nums[:-1])==0:
            return len(nums)-1
        return -1
        
