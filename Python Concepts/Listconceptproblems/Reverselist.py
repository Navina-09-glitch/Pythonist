n=int(input("Enter the number"))
if(n<=0):
    print("The number cannot be less than 0")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter the number"))
        lst.append(val)
    print(lst)
    lst.reverse()
    print("reversed list",lst)
