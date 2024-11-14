x=int(input())
y= (x*10)/100
y1=x-y
y2=x-100
if y2>0 and y1>y2:
    print(int(y2))
else:
    print(int(y1))
