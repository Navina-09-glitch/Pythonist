class student:
    crs="PYTHON"
    city="HYD"
#here crs and city are called class level data members
#Main program
#Create two objects
s1=student()
s2=student()
#Access the class level data members w.r.t objectname
print("-"*50)
print("Student course=",s1.crs)
print("Student city=",s1.city)
print("-"*50)
print("content of s1=",s1.__dict__)
print("Number of values in s1=",len(s1.__dict__))
#Program for Demonstrating the Class Level Data Members
print("content of s2=",s2.__dict__)
print("Number of values in s2=",len(s2.__dict__))
print("-"*50)