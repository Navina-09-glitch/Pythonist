n=int(input("enter number"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=[]
    for i in range(n+1):
        val=float(input("enter {}:".format(i)))
        lst.append(val)
    print(lst)

uniquelist=set(lst)
print("unique elements are ",uniquelist)
