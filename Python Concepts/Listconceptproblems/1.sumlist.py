n=int(input("Enter the number of elements"))
if n<=0:
    print("The list cannot be empty")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter the value of elements"))
        lst.append(val)
    print("the list has been added to it",lst)
    total=sum(lst)
    print("The sum of elements is",total)
