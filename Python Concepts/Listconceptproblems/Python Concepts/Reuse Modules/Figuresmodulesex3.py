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
                            Circle.area()
                        case "P":
                            Circle.peri()
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
                            Square.area()
                        case "P":
                            Square.peri()
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
                            Rect.area()
                        case "P":
                            Rect.peri()
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
                            Triangle.area()
                        case "P":
                            Triangle.peri()
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