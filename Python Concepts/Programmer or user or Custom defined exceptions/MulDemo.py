from MulTable import table
from MulExceptions import ZeroError,NegativeNumError
try:
    n=input("Enter a number for generating Mul Table: ")
    table(n)
except ZeroError:
    print("\tDont enter zero for mul table")
except NegativeNumError:
    print("\t Dont enter negative number for mul table")
except ValueError:
    print("\t Dont enter alphanumerics,str and symbols for mul table")
except:
    print("oooooops,some thing went wrong")