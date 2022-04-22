class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def bit_former(n):
            if n==1:
                return "0"
            else:
                string=bit_former(n-1)
                return string+"1"+inverter(string)[::-1]
        def inverter(s:str):
            s=list(s)
            for i in range(len(s)):
                if s[i]=="0":
                    s[i]="1"
                else:
                    s[i]="0"
            return "".join(s)
        s=bit_former(n)
       
        return s[k-1]
                
            
