#Program to accept numerical  values and find only positive values
n=int(input("Enter values"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter value"))
        lst.append(val)
    else:
        print(lst)
        pslist=[]
        for val in lst:
            if(val<=0):
                continue
            pslist.append(val)
        print(pslist)