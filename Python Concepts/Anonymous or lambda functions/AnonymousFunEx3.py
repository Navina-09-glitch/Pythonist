big=lambda a,b: a if a>b else b if b>a else "both values are equal"
#Main Program
print("Enter two values")
bv=big(float(input()),float(input()))
print("Big of two numbers is ",bv)