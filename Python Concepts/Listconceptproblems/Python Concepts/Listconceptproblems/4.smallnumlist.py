n=int(input("Enter the no of elements: "))
if(n<=0):
    print("{} is an invalid number".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter value {}: ".format(i)))
        lst.append(val)
    print(lst)
    small=lst[0]
    for x in lst:
        if x<small:
            small=x
    print("the smallest number",small)
