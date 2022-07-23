class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(x):
            minx=x[0]
            for i in x:
                if i<minx:
                    minx=i
            return Counter(x)[minx]
        ans=[0]*len(queries)
        word=[helper(i) for i in words]
        word.sort()
        for j,i in enumerate(queries):
            target=helper(i)
            l=0
            while l<len(word):
                if word[l]>target:
                    break
                l+=1
            ans[j]=len(word)-l
        return ans  
