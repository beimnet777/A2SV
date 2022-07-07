class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def myPow(x: float, n: int) -> float:
            if n==0 :
                return 1
            elif  n==1:
                return x
            else:
                res=myPow(x,n//2)
                return res*res%1000000007 if n%2==0 else res*res*x%1000000007
        if n==1:return 5
        even=(n)-(n)//2 
        odd=(n-1)-(n-1)//2 
        return (myPow(5,even)*myPow(4,odd))%1000000007
