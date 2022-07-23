class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        while l<len(haystack) and len(haystack)-l>=len(needle):
            if haystack[l:l+len(needle)]==needle:
                return l
            l+=1
        return -1
