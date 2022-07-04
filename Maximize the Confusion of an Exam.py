class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=0
        t_num=0
        f_num=0
        l,r=0,0
        last=-1
        while r<len(answerKey):
            if r !=last:
                if answerKey[r]=='T':t_num+=1
                else:f_num+=1
                last=r
            if (t_num>=f_num and f_num<=k) or (t_num<f_num and t_num<=k)  :
                ans=max(ans,t_num+f_num)
                r+=1
            else:
                if answerKey[l]=="T":
                    t_num-=1 
                else:
                    f_num-=1
                l+=1
        return ans
