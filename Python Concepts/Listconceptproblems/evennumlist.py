n=int(input("Enter the number of values: "))
if (n<=0):
    print("Invalid input {}". format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter value {}: ".format(n)))
        lst.append(val)
    print("original list", lst)
    evennumlist=[]
    for x in lst:
        if x%2==0:
            evennumlist.append(x)
    print(evennumlist)