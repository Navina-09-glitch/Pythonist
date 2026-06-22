class account:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=4.5
        self.__pin=4567
        self.bname="SBI"

print("Account number=",ac.acno) #if you put__ then only it works
print("Account name=",ac.cname)
print("Account Balance=",ac.bal)
print("Account Pin=",ac.pin)
print("Account holder branchname=",ac.bname)
#Main Program
ac=account()
#Here from Main Program we can't access Encapsulated Data members
#Mean instead of self.__acname if it was ac.acno it wont give answer so we are using other function with in the function.
#check program sameaccountclass1.py