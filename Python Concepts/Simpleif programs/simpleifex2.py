print("Enter two values")
a,b=float(input()),float(input())
if(a<b):
    print("min({},{})={}".format(a,b,a))
if(b<a):
    print("min({},{})={}".format(a,b,b))
if(a==b):
    print("min({},{})={}".format(a,b,"Both values are equal"))
print("Program execution completed")