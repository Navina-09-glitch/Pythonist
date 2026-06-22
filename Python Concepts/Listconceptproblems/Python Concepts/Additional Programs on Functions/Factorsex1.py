def findfactors(n):
    if(n<=1):
        print("{} is invalid input".format(n))
    else:
        print("Factors of {}".format(n))
        for i in range(1,n//2+1):
            if(n%i==0):
                print("\t {}".format(i))

n=int(input("enter no of factors: "))
findfactors(n)