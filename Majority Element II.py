class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        ans=[]
        for i in x.keys():
            if x[i]>(len(nums)/3):
                ans.append(i) 
        return ans 
