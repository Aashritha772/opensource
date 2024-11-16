n=int(input())
l=list(map(int,input().split(" ")))
s=set()
l1=[]
for i in l:
    if i not in s:
        l1.append(i)
        s.add(i)
print(" ".join(map(str,l1)))
