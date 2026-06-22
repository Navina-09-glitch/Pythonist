def table(n):
    if n<=0:
        print("{} is an invalid input".format(n))
    else:
        print("-"*50)
        print("Mul table for: {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("\t {}*{}={}".format(n,i,n*i))
        print("-" * 50)