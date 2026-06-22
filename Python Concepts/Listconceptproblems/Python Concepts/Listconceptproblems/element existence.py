n=int(input("enter a number"))
if(n<=0):
    print("{} is an invalid number".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter a number{}".format(i)))
        lst.append(val)
    else:
        print("list of numbers")
        print(lst)
        if val in lst:
            print("{} element exists in the list".format(val))
        else:
            print("{} element does not exists in list".format(val))
