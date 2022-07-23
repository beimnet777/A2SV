class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=set()
        y=set()
        for i in nums:
            if i not in x:
                x.add(i)
                y.add(i)
            else:
                y.remove(i)
        return y  
