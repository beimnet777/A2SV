class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[1]
        ugly, i2, i3, i5 =0, 0, 0, 0
        for i in range(n):
            ugly=min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(ugly)
            if nums[i2]*2==ugly: i2+=1
            if nums[i3]*3==ugly: i3+=1
            if nums[i5]*5==ugly: i5+=1
        return nums[n-1]          
