class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        win_set=set()
        ans = -1
        if len(s)==0:
            return 0
        while r< len(s):
            if s[r] in win_set:
                ans=max(ans,r-l)
                win_set.remove(s[l])
                l+=1
            else:
                win_set.add(s[r])
                r+=1
        ans=max(ans,r-l) 
        return ans
        
