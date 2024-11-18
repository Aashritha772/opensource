n=int(input())
l=list(map(int,input().split(" ")))
r=l[1:]+l[0:1]
for i in r:
    print(i,end=" ")
