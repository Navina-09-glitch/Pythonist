n=int(input("Enter the no of elements :"))
if(n<=0):
    print("The no of elements cannot be less than zero")
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("Enter value :".format(i)))
        lst.append(val)
    print(lst)
    m=int(input("Enter the no of elements to remove :"))
    removelst=[]
    for i in range(1,m+1):
        x=int(input("Enter value to remove :".format(i)))
        removelst.append(x)
    print(removelst)
    updatedlst=[]
    for i in lst:
        if i not in removelst:
            updatedlst.append(i)
    print(updatedlst)
    # New logic: check if any entered element was not in the list
    for x in removelst:
        if x not in lst:
            print("{} not in the original list".format(x))
    print("updated list", updatedlst)
