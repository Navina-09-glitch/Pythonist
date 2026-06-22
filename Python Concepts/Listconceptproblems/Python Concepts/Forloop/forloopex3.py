n=input("enter number for generating multiplication table")
if(n.isdigit()):
    n=int(n)
    if(n<=0):
        print("{} is an invalid input".format(n))
    else:
        print("\tmul table for:{}".format(n))
        for i in range(1,11):
            print("\t ({} x {})={}".format(n,i,n*i))
        else:
            print("-"*50)
else:
    print("{} is an invalid input".format(n))