#Program for demonstrating data abstraction
#otherprog4.py
from account4 import account
ac=account()
ac.____init__() #Method by this example, we understand contructors are not possible to hide. we can only hide instance members and instance methods
print("-"*40)
print("Account number=",ac.acno)
print("Account holder name=",ac.cname)
print("Account balance=",ac.bal)
print("Account pin=",ac.pin)
print("Account holder branch name=",ac.bname)
