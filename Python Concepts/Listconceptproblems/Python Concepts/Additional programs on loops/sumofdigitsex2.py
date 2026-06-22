num=int(input("enter number"))
if(num<=0):
    print("{} is invalid input".format(num))
else:
    tn=num
    ds=0
    while(num>0):
        d=num%10
        ds=ds+d
        num=num//10
    else:
        print("sum of digits ({})={}".format(tn,ds))