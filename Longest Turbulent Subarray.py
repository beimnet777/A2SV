class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,p,r=0,0,1
        sign=0
        ans=1
        while r<len(arr):
            if sign>0:
                if arr[p]-arr[r]>=0:
                    l=p
                    sign=0
                    continue
                else:
                    ans=max(ans,r-l+1)
                    p+=1
                    sign=-1
            elif sign <0:
                if arr[p]-arr[r]<=0:
                    l=p
                    sign=0
                    continue
                else:
                    ans=max(ans,r-l+1)
                    p+=1
                    sign=1
            else:
                if arr[p]-arr[r]>0 :
                    ans=max(ans,r-l+1)
                    p+=1
                    sign=1
                elif arr[p]<arr[r]:
                    ans=max(ans,r-l+1)
                    p+=1
                    sign=-1
                else:
                    l,p=p+1,p+1  
            r+=1
        return ans 
