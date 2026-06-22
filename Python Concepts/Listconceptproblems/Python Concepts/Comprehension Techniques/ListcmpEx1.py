#Program for finding square,cube, square root of every element of list
#list comprehensionEx1.py

lst=[12,4,15,8,-5,0,17]
print("Given list",lst)
sqlst=[]
for val in lst:
    sqlst.append(val**2)
print("Square list={}".format(sqlst))


#Using list comprehension
culist=[val**3 for val in lst]
print("Cube list={}".format(culist))

squareroot=[val**0.5 for val in lst]
print("Square root of list={}".format(squareroot))

#convert two list objects in to one list
#lst1=[10,20,30,40]
#lst2=["RS","TR","DR","SR"]
#z=zip(lst1,lst2)
#print(z,type(z))
#This will store the data as below
#10 RS
#20 TR
#30 DR
#40 SR
#if we write for x in z for loop it will take only 10 , but not 10 RS
#so write as for x,y in z
#for x in z:
    #print(x)
#for x,y in z:
    #print(x,y)
for original_value,square_value in zip(lst,sqlst):
    if(type(square_value)!=complex):
        print("\t{}\t\t\t{}".format(original_value,square_value))
    else:
        print("\t{}\t\t\t{}".format(original_value,square_value))
print("-"*50)