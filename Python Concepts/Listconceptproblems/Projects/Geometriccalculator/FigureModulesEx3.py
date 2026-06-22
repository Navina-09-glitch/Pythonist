from Figuremenu import menu
import circlefig,rectfig,squarefig,trianglefig
from subfigmenu import submenu
while(True):
    menu()
    ch=input("Enter your choice:")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                while(True):
                    submenu("circle")
                    ch=input("Enter your choice:")
                    match(ch.upper()):
                        case "A":
                            circlefig.area()
                        case "P":
                            circlefig.peri()
                        case "M":
                            break
                        case _:
                            print("your selection of submenu operation is wrong--try again")
            case 2:
                while (True):
                    submenu("triangle")
                    ch = input("Enter your choice:")
                    match (ch.upper()):
                        case "A":
                            trianglefig.area()
                        case "P":
                            trianglefig.peri()
                        case "M":
                            break
                        case _:
                            print("your selection of submenu operation is wrong--try again")
            case 3:
                while (True):
                    submenu("Rectangle")
                    ch = input("Enter your choice:")
                    match (ch.upper()):
                        case "A":
                            rectfig.area()
                        case "P":
                            rectfig.peri()
                        case "M":
                            break
                        case _:
                            print("your selection of submenu operation is wrong--try again")
            case 4:
                while (True):
                    submenu("square")
                    ch = input("Enter your choice:")
                    match (ch.upper()):
                        case "A":
                            squarefig.area()
                        case "P":
                            squarefig.peri()
                        case "M":
                            break
                        case _:
                            print("your selection of submenu operation is wrong--try again")
            case 5:
                print("Thanks for this program")
                break
            case _:
                print("your selection of submenu operation is wrong--try again")
    else:
        print("Dont enter alnums,strs and symbols for int choice-try again")

