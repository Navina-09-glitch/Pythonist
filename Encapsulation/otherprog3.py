from account3 import account
ac=account()
print(ac.__dict__)
ac.getaccdet()
#-----can't access because getaccdet() is encapsulated because it is made private instance method
print("-"*40)
print("Account number=",ac.acno)
print("account holder name=",ac.cname)
print("account holder balance=",ac.bal)
print("account holder pin=",ac.pin)
print("account holder balance=",ac.bname)
print("-"*40)