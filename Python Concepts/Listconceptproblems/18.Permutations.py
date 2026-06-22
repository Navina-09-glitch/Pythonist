from itertools import permutations
n=int(input("Enter the number of elements: "))
if(n<=0):
    print("{} is an invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter the {}th element: ".format(i)))
        lst.append(val)
    print("the list has been added to the list", lst)
perm = permutations(lst)
perm_list= list(perm)
print("all permutations")
for p in perm_list:
    print(p)