n=int(input("enter no of elements"))
if(n<=0):
    print("you cant enter less than zero")
else:
    lst1=[]
    lst2=[]
    for i in range(1,n+1):
        val=float(input("enter {}th element for list1".format(i)))
        lst1.append(val)
    print("elements are ",lst1)
    for i in range(1,n+1):
        val2=float(input("enter {}th element for list2".format(i)))
        lst2.append(val2)
    print("elements are ",lst2)
    for i in lst1:
        if i in lst2:
            print("common element found {} ".format(i))
