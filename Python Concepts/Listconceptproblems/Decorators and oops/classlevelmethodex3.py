class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON" #OR Student.crs="PYTHON"
        #Here crs called class level data member
    @classmethod
    def getcity(cls):
        cls.city="HYD" #OR Student.city="HYD"
        #here cls is the implicit name of class student
        #Here city is called class level data member
    def readstudvalues(self,objinfo):
        print("enter {} Student information".format(objinfo))
        self.sno=int(input("\tenter student number:"))
        self.sname=input("\tenter student name:")
        self.marks=float(input("\tenter student marks:"))
    def dispstuddata(self,objinfo):
        print("enter {} Student information".format(objinfo))
        print("\tEnter Student Number: {}".format(self.sno))
        print("\tEnter Student Name: {}".format(self.sname))
        print("\tEnter Student Marks: {}".format(self.marks))
        print("\tSTUDENT COURSE=",Student.crs)
        print("\tStudent City=",Student.city)

#Main program
#create objects of student class
s1=Student()
s2=Student()
#call class level methods w.r.t object name
s1.getcrs()
s1.getcity()
#Read the Data from s1
s1.readstudvalues("First")
#Read the data from s2
s1.readstudvalues("Second")
#Display the data of student object s1
s1.dispstuddata("First")
#Display the data of student object s2
s1.dispstuddata("Second")
