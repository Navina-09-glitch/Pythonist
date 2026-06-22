class student:
    crs="PYTHON PROG"
    city="TS-HYD"
#Main Program
s1=student()
s2=student()
#Place the instance data members by using object name-s1
print("-"*50)
s1.sno=int(input("student no:"))
s1.sname=input("student name:")
s1.marks=float(input("Enter first student marks:"))
print("-"*50)
#here sno,sname and marks are called instance data members with object s1
#place the instance data members by using object name-s2
print("-"*50)
s2.sno=int(input("student no:"))
s2.sname=input("student name:")
s2.marks=float(input("Enter second student marks:"))
print("-"*50)
#here sno,sname and marks are called instance data members with object s2
print("-"*50)
print("content of s1 object")
print("-"*50)
print("\t Student Number:{}".format(s1.sno))
print("\t Student Name:{}".format(s1.sname))
print("\t Student Marks:{}".format(s1.marks))
print("\tSTUDENT COURSE=",student.crs)
print("\tSTUDENT COURSE=",student.city)
print("-"*50)
print("Content of s2 object")
print("\tStudent Number:{}".format(s2.sno))
print("\tStudent Name:{}".format(s2.sname))
print("\tStudent Marks:{}".format(s2.marks))
print("\tSTUDENT COURSE=",student.crs)
print("\tSTUDENT CITY=",student.city)
print("-"*50)