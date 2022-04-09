import sys
class Solution:
    sys.setrecursionlimit(1500)
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        elif n<1:
            return False
        else:
            return self.isPowerOfThree(n/3)
        
        
        
