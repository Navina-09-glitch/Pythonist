class Account:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal = 4.5
        self.__pin = 4567
        self.bname="SBI"

    def __accessaccdet(self):
        print("Account Number=",self.__acno)
        print("account Holder Name=",self.cname)
        print("account holder bal=",self.__bal)
        print("account PIN=",self.__pin)
        print("account holder branch name=",self.bname)

    def getdetails(self):
        #self.accessaccdet()--------cannot access
        self.__accessaccdet() # we can access the encapsulated method in the same class with self
#Main Program
ac=Account()
#Here from Main Program we can't access encapsulated data members
#ac.__accessaccdet()---- we can't access encapsulated methods
ac.getdetails()

