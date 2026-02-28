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
        