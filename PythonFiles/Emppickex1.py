#Python Program to accept empnumber,employee name,empsal,empdesignation
#Get Emp details from KBD
import pickle,json
with open("emp1.pick","ab") as fp:
    while(True):
        empno=int(input("Enter empno: "))
        empname=input("Enter empname: ")
        empsal=float(input("Enter empsal: "))
        empdsg=input("Enter empdsg: ")
        lst=[]
        lst.append(empno)
        lst.append(empname)
        lst.append(empsal)
        lst.append(empdsg)
        pickle.dump(lst,fp)
        print("Employee data is saved in file")
        ch=input("Do you want to another record? (yes/no): ")
        if (ch.lower()=="no"):
            print("Thanks for using this program")
            break
