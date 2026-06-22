class student:pass
s1=student()
s2=student()
#place instance data members by using object name-s1
s1.sno=100
s1.sname="Rossum"
s1.marks=33.33
#place the instance data members by using object name-s2
s2.sno=200
s2.sname="Travis"
s2.city="HYD"
print("content of s1 object")
print("-"*50)
for key,val in s1.__dict__.items():
    print("\t{}-->{}".format(key,val))
print("-"*50)
print("content of s2 object")
print("-"*50)
for key,val in s2.__dict__.items():
    print("\t{}-->{}".format(key,val))
print("-"*50)

