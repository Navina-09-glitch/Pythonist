#Program for demonstrating the need of static method
#StaticMethodEx3.py
class Student:
    def getstudvals(self):
        self.sno = int(input("\tEnter Student Number:"))
        self.sname = input("\tEnter Student Name:")
        self.marks = float(input("\tEnter Student Marks:"))
class Employee:
    def getempvals(self):
        self.eno = int(input("\tEnter Employee Number:"))
        self.ename = input("\tEnter Employee Name:")
class Teacher:
    def getteachervals(self):
        self.tno = int(input("\tEnter Teacher Number:"))
        self.tname = input("\tEnter Teacher Name:")
        self.sub = input("\tEnter Teacher Subject:")
        self.exp = float(input("\tEnter Teacher Exp:"))
class Hyd:
    @classmethod
    def dispobjdata1(cls,objdata, objinfo): # Calss level method
        Hyd().dispobjdata2(objdata,objinfo) # Calling Instance Method w.r.t Name-Less object

    def dispobjdata2(self,objdata,objinfo): # instance Method
        self.dispobjdata(objdata,objinfo)# Calling static Method w.r.t self object

    @staticmethod
    def dispobjdata(objdata,objinfo):
        print("-"*50)
        print("'{}' Object Information".format(objinfo))
        print("-" * 50)
        for key,val in objdata.__dict__.items():
            print("\t{}--->{}".format(key,val))
        print("-" * 50)

#Main Program,
#Create an object of Student, Employee and Teacher
s=Student()
e=Employee()
t=Teacher()
#read the values for student object
s.getstudvals()
#read the values for Employee object
e.getempvals()
#read the values for Teacher object
t.getteachervals()
#Display the Values of any Object of any Calsss.
#This Can be done by Static Method
#Calling Class level method w.r.t Class Name
Hyd.dispobjdata1(s,"Student")
Hyd.dispobjdata1(e,"Employee")
Hyd.dispobjdata1(t,"Teacher")
