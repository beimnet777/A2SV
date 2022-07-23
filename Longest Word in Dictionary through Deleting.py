class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def negative(x):
            return -len(x)
        ans=[]
        dictionary.sort(key= negative)
        for i in dictionary:
            l,r=0,len(i)-1
            ls,rs=0,len(s)-1
            while ls<=rs and l<len(i) and r>-1:
                if i[l]==s[ls]:
                    l+=1
                if i[r]==s[rs]:
                    r-=1
                ls+=1
                rs-=1
                if l>r:
                    break
            if l>r:
                if len(ans)==0:  
                    ans.append(i)
                elif len(i)==len(ans[0]):
                     ans.append(i)
                else:
                    break
        return sorted(ans)[0] if len(ans) >0 else ""
