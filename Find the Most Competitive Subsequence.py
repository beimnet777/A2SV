class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack=[]
        for j,i in enumerate(nums):
            # if len(stack)==k:
                
            while stack and stack[-1]>i and len(nums)-j>=k-len(stack)+1:
                stack.pop()
            stack.append(i)
        return stack[:k]
        
