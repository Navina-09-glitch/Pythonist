class student:pass
#Main program
student.crs = "PYTHON"
student.city = "HYD"
#here crs and city are called class level data members
#create two objects
s1=student()
s2=student()
#Access the class level data members with respect to classname
print("-"*50)
print("Student Course=",student.crs)
print("student city=",student.city)
print("-"*50)
print("content of s1=",s1.__dict__)
print("Number of values in s1=",len(s1.__dict__))
print("content of s2=",s2.__dict__)
print("Number of values in s2=",len(s2.__dict__))