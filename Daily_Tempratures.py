class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[(temperatures[0],0)]
        for i in range(1,len(temperatures)):
            if temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i],i))
            else:
                while len(stack)>0 and stack[-1][0]<temperatures[i] :
                    val,index=stack.pop()
                    ans[index]=i-index
                stack.append((temperatures[i],i))
        return ans
                     
