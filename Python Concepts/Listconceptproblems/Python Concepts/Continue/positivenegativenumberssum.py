n=int(input("Enter n:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {}:".format(i)))
        lst.append(val)
    else:
        print(list)
        pslist=[]
        pssum=0
        nglist=[]
        ngsum=0
        for i in lst:
            if(i>0):
                pslist.append(i)
                pssum=i+pssum
            else:
                nglist.append(i)
                ngsum=ngsum+i
        else:
            print("positive elements are {}".format(pslist))
            print("negative elements are {}".format(nglist))
            print("positive numbers sum is {}".format(pssum))
            print("negative numbers sum is {}".format(ngsum))

