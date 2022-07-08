class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        li=list(str(abs(num)))
        if num>0:
            li.sort()
            ctr=0
            for i,j in enumerate(li):
                if int(li[i])!=0:
                    ctr=i
                    break
            temp=li[ctr]
            li[ctr]=li[0]
            li[0]=temp
            return int("".join(li))
        else:
            li.sort(reverse=True)
            x="".join(li)
            x="-"+x
            return int(x)
