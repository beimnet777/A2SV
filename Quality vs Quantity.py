def is_pos(x):
    x.sort()
    l,r,l_sum,r_sum=0,len(x)-1,x[0],x[len(x)-1]
    while l<r:
        if l+1>len(x)-r and r_sum>l_sum:
            return True
        elif l+1<=len(x)-r:
            l+=1
            l_sum+=x[l]
        elif l+1>len(x)-r and r_sum<=l_sum:
            r-=1
            r_sum+=x[r]
    return



t=input()
for _ in range(int(t)):
    first=input().split()
    second=input().split()
    num=[int(i) for i in second]
    if is_pos(num):
        print("YES")
    else:
        print("NO")
