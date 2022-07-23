class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack=[nums[0]]
        ctr=1
        ans=0
        while ctr<len(nums):
            n=len(stack)
            if n%2!=0:
                if stack[-1]!= nums[ctr]:
                    stack.append(nums[ctr])
                else:
                    ans+=1
                    ctr+=1
                    continue
            else:
                stack.append(nums[ctr])
            ctr+=1
        return ans if len(stack)%2==0 else ans+1
