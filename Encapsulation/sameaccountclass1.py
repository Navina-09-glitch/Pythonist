class account:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=4.5
        self.__pin=4567
        self.bname="SBI"
    def accessaccdet(self):
        print("Account number=",self.__acno)  # if you put__ then only it works
        print("Account name=", self.cname)
        print("Account Balance=",self.__bal)
        print("Account Pin=", self.__pin)
        print("Account holder branchname=",self.bname)
# Main Program
ac = account()
#Here from main program we can't access encapsulated data members
ac.accessaccdet()
