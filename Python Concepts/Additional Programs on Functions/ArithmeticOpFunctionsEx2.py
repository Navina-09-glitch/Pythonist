def menu():
    print("*"*50)
    print("\t\t menu options:")
    print("\t\t 1.Addition")
    print("\t\t 2.Subtraction")
    print("\t\t 3.Multiplication")
    print("\t\t 4.Division")
    print("\t\t 5.Modulo Division")
    print("\t\t 6.Exponentiation")
    print("\t\t 7.Exit")
    print("*"*50)
def addop():
    print("\t\t Enter two values of addition")
    a,b= float(input("Enter a:")),float(input("Enter b:"))
    print("\t\t sum({},{})={}".format(a,b,a+b))

def subop():
    print("\t\t Enter two values of subtraction")
    a,b= float(input("Enter a:")),float(input("Enter b:"))
    print("\t\t sub({},{})={}".format(a,b,a-b))

def mulop():
    print("\t\t Enter two values of multiplication")
    a,b= float(input("Enter a:")),float(input("Enter b:"))
    print("\t\t mul({},{})={}".format(a,b,a*b))

def divop():
    print("\t\t Enter two values of division")
    a,b= float(input("Enter a:")),float(input("Enter b:"))
    print("\t\t div({},{})={}".format(a,b,a/b))

def modop():
    print("\t\t Enter two values of modulo")
    a,b= float(input("Enter a:")),float(input("Enter b:"))
    print("\t\t mod({},{})={}".format(a,b,a%b))

def expop():
    print("\t\t Enter two values of exponentiation")
    a,b= float(input("Enter a:")),float(input("Enter b:"))
    print("\t\t exp({},{})={}".format(a,b,a**b))

#Main Program

while(True):
    menu()
    ch=int(input("Enter your choice:"))
    if(ch.isdigit())
        match(int(ch)):
            case 1:
                addop()
            case 2:
                subop()
            case 3:
                mulop()
            case 4:
                divop()
            case 5:
                modop()
            case 6:
                expop()
            case 7:
                print("Thanks for using this program")
                break
            case _:
                print("your selection of operation is wrong")
    else:
        print("your selection of operation is wrong")