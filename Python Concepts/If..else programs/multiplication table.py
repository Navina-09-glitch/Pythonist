n=input("Enter a number for generating mul table")
if(n.isdigit()):
    n=int(n)
    if(n==0):
        print("{} is an invalid input".format(n))
    else:
        print("\t mul table for {}".format(n))
        i=1
        while (i<=10):
            print("\t\t {}x{}={}".format(n,n,n*i))
            i=i+1
        else:
            print("="*50)
else:
    print("Please enter digit")