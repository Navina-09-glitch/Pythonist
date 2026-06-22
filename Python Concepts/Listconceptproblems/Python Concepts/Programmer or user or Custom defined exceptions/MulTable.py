from MulExceptions import ZeroError,NegativeNumError
def table(n1):
    n=int(n1) #Type Casting-----Chance of getting exception---ValueError
    if(n==0):
        raise ZeroError
    elif(n<0):
        raise NegativeNumError
    if(n>0):
        print("-"*50)
        print("Mul table for {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("\t\t{}x{}={}".format(n,i,n*i))
        print("="*50)

