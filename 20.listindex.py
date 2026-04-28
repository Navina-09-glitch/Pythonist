n=int(input("Enter a number:"))
if n<=0:
    print("the list cannot be empty")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter a number:"))
        lst.append(val)
    print("the list has been added to list",lst)
k=int(input("Enter a number:"))
pos=lst.index(k)
print("Index of k:",pos)