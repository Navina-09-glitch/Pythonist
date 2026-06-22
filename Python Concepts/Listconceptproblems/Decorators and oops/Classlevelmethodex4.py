class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON" #or Student.crs="PYTHON"
        #Here crs called class level data member
    @classmethod
    def getcity(cls):
        cls.city="BANG" #OR Student.city="HYD"
        #here city is called Class level data member
    def readstudvalues(self,objinfo):
        print("Enter {} student information".format(objinfo))
        self.sno=int(input("Enter student no. "))
        self.sname=input("Enter student name. ")
        self.marks=float(input("Enter student marks. "))
    def dispstuddata(self,objinfo):
        #call class level methods w.r.t self
        self.getcrs()
        self.getcity()
        print("Enter {} student information".format(objinfo))
        print("\tEnter student number:{}".format(self.sno))
        print("\tEnter student name:{}".format(self.sname))
        print("\tEnter student marks:{}".format(self.marks))
        print("\tSTUDENT COURSE=",Student.crs)
        print("\tStudent City=",Student.city)

#main program
#create objects of student class
s1=Student()
s2=Student()
#Read the data from s1
s1.readstudvalues("First")
#Read the data from s2
s2.readstudvalues("Second")
#Display the Data of Student Object s1
s1.dispstuddata("First")
#Display the Data of Student Object s2
s2.dispstuddata("Second")