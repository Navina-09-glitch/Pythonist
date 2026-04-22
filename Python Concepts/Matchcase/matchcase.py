import sys
print("\t arithmetic operations")
print("\t\t1.addition")
print("\tt2.subtraction")
print("\t\t3.multiplication")
print("\t\t4.division")
print("\t\t5.modulo division")
print("\t\t6.exponentiation")
print("\t\t7.exit")
ch=int(input("enter choice: "))
match(ch):
    case 1:
        print("Enter two values for addition")
        a,b=float(input()),float(input())
        print("\t\t sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter two values for subtraction")
        a,b=float(input()),float(input())
        print("\t\t sum({},{})={}".format(a,b,a-b))
    case 3:
        print("Enter two values for multiplication")
        a,b=float(input()),float(input())
        print("\t\t mul({},{})={}".format(a,b,a*b))
    case 4:
        print("Enter two values for division")
        a,b=float(input()),float(input())
        print("\t\t Normaldiv({},{})={}".format(a,b,a/b))
        print("\t\t Floordiv({},{})={}".format(a, b, a // b))
    case 5:
        print("Enter two values for modulodivision")
        a,b=float(input()),float(input())
        print("\t\t modulodiv({},{})={}".format(a,b,a%b))
    case 6:
        print("Enter two values for exponentiation")
        a,b=float(input()),float(input())
        print("\t\t exp({},{})={}".format(a,b,a**b))
    case 7:
        print("Thanks for using matchcase program")
        sys.exit()
    case _:
        print("Sorry, please enter a valid choice")
print("match case completed")