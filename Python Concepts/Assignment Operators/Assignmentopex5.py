a,b=int(input("Enter value of a:")),int(input("Enter value of b:"))
print("original value of a={}".format(a))
print("original value of b={}".format(b))
a=a^b
b=a^b
a=a^b
print("swapped value of a={}".format(a))
print("swapped value of b={}".format(b))