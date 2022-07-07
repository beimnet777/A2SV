class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(i):
            if i==len(s)//2:
                return
            else:
                s[i],s[-(i+1)]=s[-(i+1)],s[i]
                return helper(i+1)
        helper(0)
