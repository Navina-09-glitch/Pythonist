n=int(input("Enter the number of elements:"))
if(n<=0):
    print("Invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter value {}:".format(i)))
        lst.append(val)
    print("original lst",lst,type(lst),id(lst))
lst2_shallow=lst.copy()
print("copied list",lst2_shallow)