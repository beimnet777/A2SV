class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=''
        for  i in range(min(len(word2),len(word1))):
            ans+=word1[i]
            ans+=word2[i]
        if len(word1)>len(word2):
            for i in range(len(word2),len(word1)):
                ans+=word1[i]
        else:
            for i in range(len(word1),len(word2)):
                ans+=word2[i]
        return ans
