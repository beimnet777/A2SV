class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_forward=[]
        product_reverse=[]
        ans=[]
        prof=1
        pror=1
        for i in range(len(nums)):
            prof*=nums[i]
            pror*=nums[-(i+1)]
            product_forward.append(prof)
            product_reverse.append(pror)
        product_reverse.reverse()
        for i in range(len(nums)):
            if i>0 and i+1<len(nums):
                ans.append(product_forward[i-1]*product_reverse[i+1])
            elif i+1==len(nums):
                ans.append(product_forward[i-1])
            else:
                ans.append(product_reverse[i+1])          
        return ans
