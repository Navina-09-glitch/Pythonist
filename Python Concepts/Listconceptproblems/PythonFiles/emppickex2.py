import pickle,sys
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\PythonProject1\\Python Concepts\\Programmer or user or Custom defined exceptions")
from NameValidations import validate
from NameExceptions import InvalidNameError,ZeroLengthNameError,SpaceError
def saveempdata():
    with open("emp1.pick","ab") as fp:
        while(True):
            try:
                empno=int(input("Enter employee number: "))
                empname =validate(input("Enter employee name: "))
                empsal=float(input("Enter employee salary: "))
                empdsg=input("Enter employee designation: ")
                lst=[]
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                lst.append(empdsg)
                pickle.dump(lst,fp)
                print("List of employee records saved in a file:")
                ch=input("Do you want to save the records? (y/n): ")
                if (ch.lower()=="n"):
                    print("Thanks for this program")
                    break
            except (ValueError,InvalidNameError,ZeroLengthNameError,SpaceError) as e:
                print("try again")

saveempdata()