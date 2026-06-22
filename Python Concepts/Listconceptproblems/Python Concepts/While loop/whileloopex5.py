n=int(input("enter a number"))
if(n<=0):
    print("{} is an invalid input".format(n))
else:
    print("natural numbers with in {}".format(n))
    i=1
    sum=0
    while(i<=n):
        sum=sum+i
        i=i+1
    else:
        print("sum={}".format(sum))