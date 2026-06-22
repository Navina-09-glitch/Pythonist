n=int(input("Enter the no of elements :"))
lst=[]
if(n<=0):
    print("invalid input {}".format(n))
else:
    for i in range(n+1):
        val=float(input("Enter value {}:".format(i)))
        lst.append(val)
    print(lst)
if(len(lst)==0):
    print("list is empty")
else:
    print("list is not empty")
