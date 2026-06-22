from MulTable import table
from MulExceptions import ZeroError,NegativeNumError
while(True):
    try:
        n=input("Enter a number for generating mul table:")
        table(n)
    except ZeroError:
        print("\tDont Enter Zero for Mul Table")
    except NegativeNumError:
        print("\tDont Enter negative numbers for Mul Table")
    except ValueError:
        print("\tDont Enter alnums,strs and symbols for mul table")
    except:
        print("ooops,some thing went wrong")
    else:
        ch=input("Do you want to generate another mul table?(y/n)")
        if(ch.lower()=="no"):
            print("Thx for this program")
            break