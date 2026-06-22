 n=int(input("enter number of elements to be in list"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("enter value for {}".format(i)))
        lst.append(val)
    print(lst)

duplicate=[]
#Create a list of integers
#list=[1,2,3,2,4,5,6,1,7,8,3,9,1]

for i in lst:
    if lst.count(i)>1:
        print("{} is duplicated".format(i))
        if i not in duplicate:
            duplicate.append(i)
print("original list:",lst)
print("duplicate numbers are:",duplicate)