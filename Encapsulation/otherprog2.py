#Program for Demonstrating Data Abstraction
from account2 import account
ac=account() #object creation
print(ac.__dict__)
ac.getaccdetails()
print("-"*40)
#print("Account number:",ac.acno)
print("Account holder name:",ac.cname)
#print("Account holder bal=",ac.bal)
#print("Account PIN=",ac.pin)
print("Account Holder Branch Name=",ac.bname)
print("-"*40)