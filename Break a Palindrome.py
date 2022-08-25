class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)<2:
            return ""
        elif "a"*len(palindrome)==palindrome:
            return palindrome[0:len(palindrome)-1]+'b'
        else:
            for i,j in enumerate(palindrome):
                if j!='a':
                    ans=palindrome[0:i]+'a'+palindrome[i+1:] 
                    if ans=="a"*len(palindrome):
                        return palindrome[0:len(palindrome)-1]+'b'
                    else:
                        return ans
