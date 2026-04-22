#Multiplication table for single number
#n=int(input("enter the number"))
#if(n<=0):
    #print("{}is invalid".format(n))
#else:
    #for i in range(1,11):
        #print("\t{}x{}={}".format(n,i,n*i))


#Multiplication table for generating for 1 to n where n is positive
n=int(input("enter the number"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    for num in range(1,n+1):
        print("Multiplication table for:{}".format(num))
        for i in range (1,11):
            print("\t{} * {} = {}".format(num,i,num*i))