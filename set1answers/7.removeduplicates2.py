n=int(input("enter no of elements:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=[]
    for i in range(n+1):
        val=float(input("enter {}:".format(i)))
        lst.append(val)
    print(lst)
uniquelist=[]
for item in lst:
    if item not in uniquelist:
        uniquelist.append(item)
print("list after removal of duplicates:",uniquelist)

