
#12.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
		#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
		#Expected Output : ['Green', 'White', 'Black']

n=int(input("enter number of words"))
if(n<=0):
    print("input is invalid")
else:
    lst=[]
    for i in range(n):
        val=input("enter {}th word".format(i)) # word is string
        lst.append(val)
    print(lst)
    lst.pop(5)
    lst.pop(4)
    lst.pop(0)
    print(lst)

#we can use pop but it removes only the last element of list
#del lst[5]
#del lst[4]
#del lst[0]
# pop and del will remove values by index and del can also remove by value

