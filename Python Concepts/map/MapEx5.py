def sumop(x,y):
    return x+y
print("Enter first list elements")
lst1=list(map(float,input().split()))
print("Enter second list elements")
lst2=list(map(float,input().split()))
#add two list objectsby using map()
lst3=list(map(sumop,lst1,lst2))
print("*"*50)
print("\tlist1\t\tlist2\t\tsumlist")
for val1,val2,val3 in zip(lst1,lst2,lst3):
    print("\t{}\t\t\t{}\t\t\t{}".format(val1,val2,val3))
print("-"*50)