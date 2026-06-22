print("Enter list of values separated by space:")
oldsal=list(map(float,input().split()))
#Give 50% Hike all employees
newsal=list(map(lambda sal:sal+sal*50/100,oldsal))
print("\tOld salary\tNew salary")
for osl,nsl in zip(oldsal,newsal):
    print("\t{}\t\t\t{}".format(osl,nsl))
print("-"*50)
