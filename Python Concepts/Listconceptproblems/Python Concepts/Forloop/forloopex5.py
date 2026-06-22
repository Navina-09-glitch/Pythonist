n=int(input("Enter a number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    s=0
    for i in range(1,n+1):
        val=float(input("Enter {}:".format(i)))
        s=s+val
    else:
        print("sum={}".format(s))
        print("Average=%0.2f"%(s/n))