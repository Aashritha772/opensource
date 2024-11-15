x,n=map(int,input().split(" "))
n1=n//100
if n1>x:
    if n%100==0:
        n2=(n1-x)
    else:
        n2=(n1-x)+1
    print(n2)
else:
    print("0")
