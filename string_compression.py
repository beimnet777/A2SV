class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        i=0
        amount=1
        j=1
        while j<len(chars):
            if chars[i]==chars[j]:
                amount+=1
            else:
                s+=(chars[i])
                if amount==1:
                    pass 
                else:
                    s+=str(amount)  
                i=j
                amount=1 
            j+=1
        
        if amount==1:
            s+=(chars[i])
        else:
            s+=(chars[i])
            s+=str(amount)
        
        len1=len(s)
        len2=len(chars)
        diff=len2-len1
        for i in range(len1):
            chars[i]=s[i]
        for i in range(diff):
            chars.pop(-1)
        return len1    
