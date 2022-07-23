class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=0
        r=k-1
        count=0
        vowles=set(['a','e','i','o','u'])
        for i in range(k):
            if s[i] in vowles:
                count+=1
        ans=count
        print(count)
        while r<len(s)-1:
            if s[l] in vowles:
                count-=1
            l+=1
            r+=1
            if s[r] in vowles:
                count+=1
            ans=max(ans,count)
        return ans    
