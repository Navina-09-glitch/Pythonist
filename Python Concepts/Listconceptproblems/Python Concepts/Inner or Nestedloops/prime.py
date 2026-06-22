n=int(input("enter range in which primes will be displayed"))
if(n<=1):
    print("{} is invalid".format(n))
else:
    print("list of prime numbers up to {}".format(n))
    nop=0
    for num in range(2,n+1):
        res=True
        for i in range(2,num):
            if num%i==0:
                res=False
                break
        if res==True:
            print("{} is prime".format(num))
            nop=nop+1
    else:
        print("number of primes with in {}".format(n,nop))