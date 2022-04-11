class Solution:
    def isValid(self, s: str) -> bool:
        dict={"(":")","[":"]","{":"}"}
        stack=[]
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                elif i !=dict[stack.pop()]:
                    return False
        if len(stack)==0:
            return True
        return False
        
