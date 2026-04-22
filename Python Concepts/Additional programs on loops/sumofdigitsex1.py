num=int(input("enter a number"))
if(num<=0):
    print("{} is invalid input")
else:
    ds=0
    for d in str(num):
        ds=ds+int(d)
    else:
        print("sum of digits ({})={}".format(num,ds))