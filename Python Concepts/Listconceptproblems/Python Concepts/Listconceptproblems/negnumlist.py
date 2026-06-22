n=int(input("Enter the no of elements :"))
if(n<=0):
    print("The no of elements cannot be less than zero")
else:
    lst=[]
    for i in range(1,n+1):
        val=int(input("Enter value :".format(i)))
        lst.append(val)
    print(lst)
for num in lst:
    if num<0:
        print(num,end=" ")