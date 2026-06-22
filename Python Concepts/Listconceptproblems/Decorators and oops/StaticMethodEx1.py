class Student():
    def getstudvals(self):
        self.sno=int(input("\tEnter student number:"))
        self.name=input("\tEnter student name:")
        self.marks=int(input("\tEnter student marks:"))
class Employee():
    def getempvals(self):
        self.eno=input("\tEnter employee name:")
        self.ename=input("\tEnter employee name:")
class Teacher:
    def getteachervals(self):
        self.tno=int(input("\tEnter teacher number:"))
        self.tname=input("\tEnter teacher name:")
        self.sub=input("\tEnter teacher subject:")
        self.exp=float(input("\tEnter teacher experience:"))
class Hyd:
    @staticmethod
    def dispobjdata(objdata,objinfo):
        print("'{}'object information".format(objinfo))
        print("-"*50)
        for key,value in objdata.__dict__.items():
            print("{}={}".format(key,value))
        print("-"*50)
#Main Program
#Create an object of student, employee and Teacher
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
#Calling static method w.r.t Class Name
Hyd.dispobjdata(s,"Student")
Hyd.dispobjdata(e,"Employee")
Hyd.dispobjdata(t,"Teacher")
