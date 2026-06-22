#Program for Demonstrating the Class Level Data Members
#ClassLevelMethodEx1.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON" #OR Student.crs="PYTHON"
        cls.city="HYD" # OR Student.city="HYD"
        # Here crs and city are called Class Level Data Members

#Main Program
#Call Class Level Method w.r.t Class Name
Student.getcrs()
#Create Objects
s1=Student()
s2=Student()
print("------------------------------------")
print("content of s1=",s1.__dict__)
print("content of s2=",s2.__dict__)
print("------------------------------------")
print("Student Course=",Student.crs)
print("Student City=",Student.city)
print("---------------OR---------------------")
print("Student Course=",s2.crs)
print("Student City=",s2.city)
