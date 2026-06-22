n=int(input("enter no."))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("Natural numbers with in :{}".format(n))
    i=1
    p=1
    while(i<=n):
        print("{}".format(i))
        p=p*i
        i=i+1
    else:
        print("product={}".format(p))
