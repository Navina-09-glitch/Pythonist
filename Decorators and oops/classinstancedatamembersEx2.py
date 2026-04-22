class Student:pass
#Main Program
Student.city = "New York"
Student.crs="PYTHON-PROG"
#here crs and city are called class level data member
#create two object
s1=Student()
s2=Student()
#place the instance data members by using object name-s1
print("-"*50)
s1.sno=int(input("Enter first student number:"))
s1.sname=int(input("Enter first student name:"))
s1.marks=int(input("Enter first student marks:"))
#here sno,sname and marks are called instance data members with object s1
print("-"*50)
#place instance data members by using object name-s2
s2.sno=int(input("Enter second student number:"))
s2.sname=int(input("Enter second student name:"))
s2.marks=int(input("Enter second student marks:"))
print("-"*50)
print("content of s1 object")
print("\t student number:{}".format(s1.sno))
print("\t student name:{}".format(s1.sname))
print("\t student marks:{}".format(s1.marks))
print("\tSTUDENT COURSE=",student.crs)
print("\tSTUDENT CITY=",student.city)
print("-"*50)
print("content of s2 object")
print("\t student number:{}".format(s2.sno))
print("\t student name:{}".format(s2.sname))
print("\t student marks:{}".format(s2.marks))
print("\tSTUDENT COURSE=",student.crs)
print("\tSTUDENT CITY=",student.city)