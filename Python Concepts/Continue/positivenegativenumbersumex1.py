n=int(input("enter number of list of values"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter a number{}".format(i)))
        lst.append(val)
    else:
        print("list of numbers")
        print(lst)
        ps,ns=0,0
        pslist=[]
        nglist=[]
        for val in lst:
            if(val<=0):
                continue
            pslist.append(val)
            ps=ps+val
        else:
            print("positive elements are {}".format(pslist))
            print("sum of positive elements is {}".format(ps))
            for val in lst:
                if(val>=0):
                    continue
                nglist.append(val)
                ns=ns+val
            else:
                print("negative elements are {}".format(nglist))
                print("negative numbers sum is {}".format(ns))


