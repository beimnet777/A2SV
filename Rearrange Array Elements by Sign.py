class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        ans=[]
        for i in nums:
            if i>0:
                positive.append(i)
            else:
                negative.append(i)
        x=0
        while x<len(positive):
            ans.append(positive[x])
            ans.append(negative[x])
            x+=1
        return ans 
