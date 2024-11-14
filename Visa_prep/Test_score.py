n,x,y=map(int,input().split(" "))
t=n*x
if t>=y:
    if y%x==0:
        t1=y/x
        if t1<=n:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
