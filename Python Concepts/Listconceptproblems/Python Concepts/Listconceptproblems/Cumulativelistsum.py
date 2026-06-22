n=int(input("enter number of elements to be in list"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter value for {}".format(i)))
        lst.append(val)
    print(lst)
    sum=0
    for i in lst:
            sum=sum+i
    print("sum of digits ({})={}".format(n,sum))