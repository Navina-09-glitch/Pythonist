positive=lambda lst:lst>0
negative=lambda lst:lst<0
#Main Program
print("Enter list of Elements separated by space")
x=input()
y=x.split()
lst=[]
for val in y:
    lst.append(float(val))
positive_list=[]
negative_list=[]

for num in lst:
    if num >0:
        positive_list.append(num)
    else:
        negative_list.append(num)
print("Given elements=",lst)
print("Positive=",positive_list)
print("Negative=",negative_list)