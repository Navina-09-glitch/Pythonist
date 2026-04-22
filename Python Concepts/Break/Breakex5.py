n=int(input("enter number"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    prime=True
    for i in range(2,n):
        if(n%i==0):
            prime=False
            break
    print("{} is prime".format(n) )