#Program for Demonstrating the Class Level Data Members
#ClassLevelMethodEx2.py
class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON" #OR Student.crs="PYTHON"
        #Here crs called Class Level Data Member
        cls.getcity() # calling Class Level Method w.r.t cls
    @classmethod
    def getcity(cls):
        cls.city="HYD" # OR Student.city="HYD"
        # here city is called Class Level Data Member

#Main Program
#Call Class Level Method w.r.t Class Name
Student.getcrs() # calling Class Level Method w.r.t Class name
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
print("---------------OR---------------------")
print("Student Course=",s1.crs)
print("Student City=",s1.city)
