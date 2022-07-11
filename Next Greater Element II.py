class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        ctr=0
        stack=[]
        while ctr<2*len(nums):
            index=ctr%len(nums)
            while stack and stack[-1][0]<nums[index]:
                x=stack.pop()
                if ans[x[1]]==-1:
                    ans[x[1]]=nums[index]
            stack.append((nums[index],index))
            ctr+=1
        return ans
