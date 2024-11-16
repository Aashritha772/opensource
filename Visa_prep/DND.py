n,m=map(int,input().split())
l=list(map(int,input().split()))
num1=0
num2=0
for i in range(0,n):
    if l[i]%m==0:
        num1+=l[i]
    else:
        num2+=l[i]
print(num1-num2)
