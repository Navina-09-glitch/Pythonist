def hike(sal):
    return (sal+sal*50/100)
#Main Program
print("Enter list of values separated by spaces:")
oldsal=list(map(float,input().split()))
newsal=list(map(hike,oldsal))
print("\tOld salary\tNew salary")
#When we use zip , it prints two lists in tabular form
for osl,nsl in zip(oldsal,newsal):
    print("\t{}\t\t\t{}".format(osl,nsl))
print("-"*50)
