from Figuremenu import menu
import circle,rect,square,triangle
from SubFigMenu import submenu
while(True):
    menu()
    ch=input("Enter Ur Choice:")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                while(True):
                    submenu("CIRCLE")
                    ch1=input("Enter UR Choice:")
                    match(ch1.upper()):
                        case "A":
                            circle.area()
                        case "P":
                            circle.peri()
                        case "M":
                            break
                        case _:
                            print("Ur Selection of Sub Menu Operation-wrong try again")

            case 2:
                while (True):
                    submenu("SQUARE")
                    ch1 = input("Enter UR Choice:")
                    match (ch1.upper()):
                        case "A":
                            square.area()
                        case "P":
                            square.peri()
                        case "M":
                            break
                        case _:
                            print("Ur Selection of Sub Menu Operation-wrong try again")

            case 3:
                while (True):
                    submenu("RECTANGLE")
                    ch1 = input("Enter UR Choice:")
                    match (ch1.upper()):
                        case "A":
                            rect.area()
                        case "P":
                            rect.peri()
                        case "M":
                            break
                        case _:
                            print("Ur Selection of Sub Menu Operation-wrong try again")

            case 4:
                while(True):
                    submenu("TRIANGLE")
                    ch1=input("Enter UR Choice:")
                    match(ch1.upper()):
                        case "A":
                            triangle.area()
                        case "P":
                            triangle.peri()
                        case "M":
                            break
                        case _:
                            print("Ur Selection of Sub Menu Operation-wrong try again")
            case 5:
                print("Thx for this program")
                break
            case _:
                print("UR Selection of Operation Wrong--try Again")
    else:
        print("Don't enter alnums,strs and symbols for int Choice-try again")