n=int(input("enter numbers:"))
if(n<0):
        print("try again")
else:
    lst=[]
    ulist=[]
    for i in range(1,n+1):
        val=float(input("enter value:{}".format(i)))
        lst.append(val)
    print(lst)
    #ulist=list(set(lst))
    #print("unique values",ulist)
    for x in lst:
        if x not in ulist:
            ulist.append(x)
    print(ulist)