n=int(input("enter no of numbers"))
if(n<2):
    print("Second largest number cannot be found (need at least 2 elements)".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter {}th number".format(i)))
        lst.append(val)
    print(lst)
    unique_lst=list(set(lst))
    unique_lst.sort(reverse=True) #descending order
    print(unique_lst)
    if (len(unique_lst)>2):
        print("Second largest number is",unique_lst[1])
    else:
        print("all numbers are same")
