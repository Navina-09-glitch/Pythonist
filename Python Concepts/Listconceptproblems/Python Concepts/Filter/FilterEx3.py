positive=lambda val: val>0
negative=lambda val: val<0
#Main Program
x=input("Enter list of Elements separated by space")
lst=[]
for val in x.split():
    lst.append(float(val))
pslist=list(filter(positive,lst))
nglist=list(filter(negative,lst))
print("positive elements=",pslist)
print("negative elements=",nglist)
