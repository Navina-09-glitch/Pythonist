#Program for Demonstrating the Class Level Data Members
#ClassLevelDataMembersEx1.py
class Student:
    crs="PYTHON"
    city="HYD"# here crs and city  are called Class Level Data Member
#Main Program
#Create Two Objects
s1=Student()
s2=Student()
#Access the Class Level Data Members w.r.t Class Name
print("--------------------------------------")
print("Student Course=",Student.crs)
print("Student City=",Student.city)
print("--------------------------------------")
print("Content of s1=",s1.__dict__)
print("Number of Values in s1=",len(s1.__dict__))
print("--------------------------------------")
print("Content of s2=",s2.__dict__)
print("Number of Values in s2=",len(s2.__dict__))
print("--------------------------------------")