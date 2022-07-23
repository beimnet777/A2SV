class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def helper(i):
            if i==0:
                return False
            elif i==1:
                return True
            else:
                if i%2 !=0:
                    return False
                else:
                    return helper(i//2)
        x=helper(n)
        print(x)
        return x
