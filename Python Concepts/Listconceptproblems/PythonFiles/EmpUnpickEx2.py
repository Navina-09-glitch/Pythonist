#Program for Reading Employee Records from Employee File (emp.pick)
#EmpUnPickEx2.py
import pickle
def readempdata():
    with open("emp.pick","rb") as fp:
        print("----------------------------------")
        print("List of Employee Records")
        print("----------------------------------")
        while(True):
            try:
                record = pickle.load(fp)
                for val in record:
                    print(val,end="\t\t")
                print()
            except EOFError:
                print("----------------------------------")
                break

#Main Program
readempdata()