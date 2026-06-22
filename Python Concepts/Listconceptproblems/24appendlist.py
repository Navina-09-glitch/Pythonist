# Program to create two lists from user input and append the first list to the second list
n1=int(input("enter number of elements for the first list:"))
if (n1<=0):
    print("{} is an invalid input".format(n1))
else:
    list1=[]
    for i in range(1,n1+1):
        val=float(input("enter value:{} for first list".format(i)))
        list1.append(val)
    print("first list:{}",list1)
n2= int(input("enter number of elements for the second list:"))
if (n2<= 0):
    print("{} is an invalid input".format(n2))
else:
    list2=[]
    for i in range(1,n2+1):
        val=float(input("enter value:{} for second list".format(i)))
        list2.append(val)
    print("original list2:{}",list2)
    for item in list1:
        list2.append(item)
    print("second list after appending:{}",list2)


