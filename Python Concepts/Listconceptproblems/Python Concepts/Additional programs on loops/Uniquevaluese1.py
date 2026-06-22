#Program for accepting list of values and obtains unique value
n=int(input("enter number of values"))
if(n<=0):
    print("\t {} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter number {}".format(i)))
        lst.append(val)
    else:
        print(lst)
        ulist=[]
        for val in lst:
            if val not in ulist:
                ulist.append(val)
        else:
            print(ulist)