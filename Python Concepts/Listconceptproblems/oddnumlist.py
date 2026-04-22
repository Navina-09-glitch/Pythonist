n=int(input("enter range of values"))
if (n<=0):
    print("{} is an invalid number".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val = float(input("enter number"))
        lst.append(val)
    print(lst)
    oddnumlist = []
    for num in lst:
        if num%2!=0:
            oddnumlist.append(num)
    print(oddnumlist)
