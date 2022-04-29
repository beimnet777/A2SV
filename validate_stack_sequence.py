class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[pushed[0]]
        length=len(pushed)
        i=1
        j=0
        while i<length or j<length:
            if len(stack)>0:
                if popped[j]==stack[-1]:
                    stack.pop()
                    j+=1  
                else:
                    if i<length:
                        stack.append(pushed[i])
                        i+=1
                    else:
                        return False
            else:
                if i<length:
                    stack.append(pushed[i])
                    i+=1
        
        return True
        
