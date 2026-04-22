from Figuremenu import menu
import circlefig,rectfig,squarefig,trianglefig
while(True):
    menu()
    ch=input("Enter your choice:")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                circlefig.area()
                circlefig.peri()
            case 2:
                trianglefig.area()
                trianglefig.peri()
            case 3:
                squarefig.area()
                squarefig.peri()
            case 4:
                rectfig.area()
                rectfig.peri()
            case 5:
                print("Thanks for this program")
                break
            case _:
                print("Your selection was invalid")
    else:
        print("Dont enter alnums,strs and symbols for int choice--try again")