class student:pass
#Main program
s1=student()
s2=student()
#Place the instance data members by using object name-s1
print("_"*50)
s1.sno=int(input("Enter sno:"))
s1.sname=input("Enter sname:")
s1.marks=int(input("Enter marks:"))
#Place the instance data members by using object name-s2
print("_"*50)
s2.sno=int(input("Enter sno:"))
s2.sname=input("Enter sname:")
s2.marks=int(input("Enter marks:"))
print("content of s1 object")
print("\tStudent Number:{}".format(s1.sno))
print("\tStudent Name:{}".format(s1.sname))
print("\tStudent Marks:{}".format(s1.marks))
print("content of s2 object")
print("\tStudent Number:{}".format(s2.sno))
print("\tStudent Name:{}".format(s2.sname))
print("\tStudent Marks:{}".format(s2.marks))