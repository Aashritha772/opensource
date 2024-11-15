n=int(input())
l=map(int,input().split(" "))
k=int(input())
s=set()
c=False
for i in l:
    if (k-i) in s:
        c=True
        break
    s.add(i)
if c:
    print("true")
else:
    print("false")
