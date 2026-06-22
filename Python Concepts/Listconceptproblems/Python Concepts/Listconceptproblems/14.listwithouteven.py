n=int(input("Enter the number of elements"))
if n<=0:
    print("The list cannot be empty")
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter the value of elements"))
        lst.append(val)
    print("the list has been added to it",lst)
    filtered_list=[]
    for i in lst:
        if(i%2!=0):
            filtered_list.append(i)
    print(filtered_list)