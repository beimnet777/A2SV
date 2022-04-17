class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        for i in range(len(l)):
            sub=nums[l[i]:r[i]+1]
            sub.sort()
            diff=sub[1]-sub[0]
            flag=0
            for j in range(1,len(sub)):
                if sub[j]==sub[j-1]+diff:
                    continue
                else:
                    flag=1
                    break
            if flag==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
