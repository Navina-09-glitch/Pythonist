52
n=int(input("Enter no of elements: "))
if (n<=0):
    print("Invalid no of elements".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter value {}: ".format(i)))
        lst.append(val)
    print(lst)
    large=lst[0]
    for num in lst:
        if num>large:
            large=num
    print("largest number in lst {}".format(large))