try:
    print("Program Execution started")
    s1=input("Enter value of a:")
    s2=input("Enter value of b:")
    a=int(s1)
    b=int(s2)
    c=a/b
except ZeroDivisionError as z:
    print(z)
except ValueError as kvr:
    print(kvr)
else:
    print("\ta=",a)
    print("\tb=",b)
    print("\tDiv=",c)
finally:
    print("Iam from finally block")