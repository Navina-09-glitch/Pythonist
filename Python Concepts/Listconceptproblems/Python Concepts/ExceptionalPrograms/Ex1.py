#Ex1.py
print("Program Execution started")
s1=input("\tEnter Value of a:")
s2=input("\tEnter Value of b:")
print("\ts1=",s1)
print("\ts2=",s2)
a=int(s1) #----------------------------ValueError
b=int(s2) #----------------------------ValueError
c=a/b  #-------------------------------ZeroDivisionError
print("\tDiv=",c)
print("Program Execution Ended")