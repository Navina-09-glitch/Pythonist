n=int(input("enter a number"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    sum=0
    i=1
    sqsum=0
    cubesum=0
    while(i<=n):
        print("\t {}\t\t\t\t {}\t\t\t\t {}".format(i,i**2,i**3))
        sum=sum+i
        sqsum=sqsum+i**2
        cubesum=cubesum+i**3
        i=i+1
    else:
        print("{}\t\t\t\{}t\t\t\t {}".format(sum,sqsum,cubesum))