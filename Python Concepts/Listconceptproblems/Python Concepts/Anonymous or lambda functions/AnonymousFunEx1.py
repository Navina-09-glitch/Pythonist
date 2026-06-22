addop=lambda a,b:a+b
print("Type of addop=",type(addop)) #<class 'function'>
print("Enter two values")
res=addop(float(input()),float(input()))
print("Addition of two numbers is ",res) 