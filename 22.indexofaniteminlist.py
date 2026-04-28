n=int(input("Enter a number:"))
if (n<=0):
    print("{} is an invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter value:{}".format(i)))
        lst.append(val)
    print("original list:{}",lst)