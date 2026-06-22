from Figuremenu import menu
import circle,square,rect,triangle
while(True):
    menu()
    choice=int(input("enter your choice:"))
    if (ch.isdigit()):
        match(int(ch)):
            case 1:
                circle.area()
                circle.peri()
            case 2:
                square.area()
                square.perimeter()
            case 3:
                Rect.area()
                Rect.peri()
            case 4:
                triangle.area()
                triangle.peri()
            case 5:
                print("Thanks for this program")
                break
            case _:
                print("ur selection was invalid")
    else:
        print("Dont enter alnums, strs and symbols for int choice-try again")
