n=int(input("enter the number"))
if(n<=0):
    print("the list cannot be empty")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter the number"))
        lst.append(val)
    print(lst)
    lst.clear()
    print("the list has been cleared",lst)
