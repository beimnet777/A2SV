def tot_ram(x,cur):
    x.sort(key=lambda j:j[0])
    x=list(reversed(x))
    while len(x)>0 and cur >=x[-1][0]:
        ram=x.pop()
        cur+=ram[1]
    return cur


t=input()
for _ in range(int(t)):
    first=input().split()
    second=input().split()
    third=input().split()
    main=[(int(second[i]),int(third[i])) for i in range(int(first[0]))]
    print(tot_ram(main,int(first[1])))
