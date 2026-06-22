n=int(input("Enter a number for generating mul table"))
if(n<=0):
    print("Invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("Enter a number for generating mul table"))
        lst.append(val)
    else:
        print("list of values")
        print(lst)
        for num in lst:
            if(num<=0):pass
            else:
                print("Mul Table for {}".format(num))
                for i in range(1,11):
                    print("\t {} x {}".format(num,i,num*i))