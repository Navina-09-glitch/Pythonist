n=int(input("enter no."))
if(n<=0):
    print("{} is invalid".format(n))
else:
    p=1
    i=1
    while(i<=n):
        p=p*i
        i=i+1
    else:
        print("factorial ({})={}".format(n,p))
