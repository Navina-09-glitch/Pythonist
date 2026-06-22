n=int(input("Enter the number of elements:"))
if n<=0:
    print("{} is an invalid input".format(n))
else:
    lst1=[]
    for i in range(n+1):
            val=float(input("Enter the element {}:".format(i)))
            lst1.append(val)
    print("Original list1", lst1)
    lst2=[]
    for i in range(n+1):
        val=float(input("Enter the element {}:".format(i)))
        lst2.append(val)
    print("original list2", lst2)

difference= list(set(lst1) - set(lst2))
print("Difference(list1-list2):",difference)

