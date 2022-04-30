class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        stack.append(num[0])
        counter = 0
        if len(num)==k:
            return "0"
        l = 1 
        while l < len(num):
            
            if num[l] >= stack[-1]:
                stack.append(num[l])
            else:
                while stack and counter < k and num[l] < stack[-1]:
                    stack.pop()
                    counter += 1
                stack.append(num[l])
            l += 1 
        return str(int("".join(stack[:len(num)-k])))
