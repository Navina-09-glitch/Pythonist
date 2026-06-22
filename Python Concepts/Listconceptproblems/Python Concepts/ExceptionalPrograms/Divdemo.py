from Division import divop
from excepts import DivisionError
try:
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    r=divop(a,b)
except DivisionError:
    print("\tDont enter zero for denominator")
except ValueError:
    print("\tDont enter Alnums,Strs and symbols")
else:
    print("Div({},{})={}".format(a,b,r))
finally:
    print("Iam from finally block")