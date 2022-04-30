class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mylist=[]
        for v,x in zip(position,speed):
            mylist.append([v,x])
        mylist.sort(reverse = True)
        stack = []    
        for value in mylist:
            if len(stack) == 0:
                stack.append( (target - value[0])/value[1])
            elif stack[-1] >= (target - value[0])/value[1]:
                continue
            elif stack[-1] < (target - value[0])/value[1]:
                stack.append( (target - value[0])/value[1])
        return len(stack)
