n=int(input())
if 1<=n<=12:
    d={"spring":{3,4,5},"Summer":{6,7,8},"Autumn":{9,10,11},"Winter":{12,1,2}}
    for keys,values in d.items():
        if n in values:
            print(keys)
            break
else:
    print("Invalid")
