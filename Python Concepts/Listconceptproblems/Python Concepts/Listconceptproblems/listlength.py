n=int(input("Enter number of list of values:"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter value for {}:".format(i)))
        lst.append(val)
    print("list of numbers")
    length=len(lst)
    print("length of list is {}".format(length))