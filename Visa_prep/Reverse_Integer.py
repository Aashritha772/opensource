n=int(input())
n1=str(n)
if n<0:
    n2= '-'+n1[:0:-1]
else:
    n2=n1[::-1]
n3=int(n2)
if (-2**31) <= n3 <= (2**31)-1:
    print(n3)
else:
    print("0")
