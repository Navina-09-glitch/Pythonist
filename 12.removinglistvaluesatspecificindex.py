
#12.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
		#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
		#Expected Output : ['Green', 'White', 'Black']

n=int(input("enter number of words"))
if(n<=0):
    print("input is invalid")
else:
    lst=[]
    for i in range(1,n+1):
        val=input("enter {}th word".format(i)) # word is string
        lst.append(val)
    print(lst)
    del lst[0]
    del lst[4]
    del lst[5]
    print(lst)

#we can use pop but it removes only the last element of list
#lst.pop(5)
#lst.pop(4)
#lst.pop(0)


