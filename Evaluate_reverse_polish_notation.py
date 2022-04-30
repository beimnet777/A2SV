class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        j=0
        while j<len(tokens):
            if tokens[j]=="*" or tokens[j]=="+" or tokens[j]=="/" or tokens[j]=="-":
                num1=int(tokens[j-2])
                num2=int(tokens[j-1])
                if tokens[j]=="*":
                    val=num1*num2
                elif tokens[j]=="/":
                    val=int(num1/num2)
                elif tokens[j]=="+":
                    val=num1+num2
                else:
                    val=num1-num2
                tokens[j-2:j+1]=[val]
                j-=1
            else:
                j+=1
        return int(tokens[0])
