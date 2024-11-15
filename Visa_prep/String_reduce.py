s=input()
l=list(s)
n=len(l)
l1=[]
i=0
while i<n:
    c=1
    while i+1<n and l[i]==l[i+1]:
        c+=1
        i+=1
    l1.append(l[i]+str(c))
    i+=1
print("".join(l1))
