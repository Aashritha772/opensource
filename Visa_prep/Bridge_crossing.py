x,y,z=map(int,input().split(" "))
if x+y<=z:
    z1=z-y
    z2=z1//x
    print(z2)
else:
    print("0")
