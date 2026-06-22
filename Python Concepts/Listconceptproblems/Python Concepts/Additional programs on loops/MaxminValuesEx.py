n=int(input("Enter a number: "))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {}: ".format(i)))
        lst.append(val)
    else:
        kvrmax=lst[0]
        kvrmin=lst[0]
        for val in lst:
            if(val>kvrmax):
                kvrmax=val
            else:
                kvrmin=val
        else:
            print("given values={}".format(lst))
            print("kvrmax={}".format(kvrmax))
            print("kvrmin={}".format(kvrmin))