class NumArray:

    def __init__(self, nums: List[int]):
        self.num=[0]*len(nums)
        for j,i in enumerate(nums):
            self.num[j]=self.num[j-1]+i
        
    def sumRange(self, left: int, right: int) -> int:
        left_sum=0 if left==0 else self.num[left-1]
        return self.num[right]-left_sum
