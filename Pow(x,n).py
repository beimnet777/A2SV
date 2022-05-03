class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0 :
            return 1
        elif  n==1:
            return x
        else:
            if n<0:
                return 1/(self.myPow(x,-n))
            else:
                res=self.myPow(x,n//2)
                return res*res if n%2==0 else res*res*x
