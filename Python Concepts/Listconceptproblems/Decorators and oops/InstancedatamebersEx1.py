class student: pass
#Main Program
s1=student()
s2=student()
print("content of s1=",s1.__dict__)
print("Number of values of s1=",len(s1.__dict__))
print("s1 object created whose id=", id(s1))
print("_"*50)
print("content of s2=",s2.__dict__)
print("Number of values of s2=",len(s2.__dict__))
print("s2 object created whose id=", id(s2))
print("_"*50)
#place Instance data members by using object name-s1
s1.sno=100
s1.sname="Rossum"
s1.marks=33.33
#place Instance data members by using object name-s2
s2.sno=200
s2.sname="Travis"
s2.city="HYD"
print("content of s1=",s1.__dict__)
print("Number of values of s1=",len(s1.__dict__))
print("s1 object created whose id=", id(s1))
print("_"*50)
print("content of s2=",s2.__dict__)
print("Number of values of s2=",len(s2.__dict__))
print("s2 object created whose id=", id(s2))
print("_"*50)