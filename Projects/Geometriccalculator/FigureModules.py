from Figuremenu import menu
from circlefig import area as ca, peri as cp
from squarefig import area as sa, peri as sp
from rectfig import area as ra, peri as rp
from trianglefig import area as ta,peri as tp
while(True):
    menu()
    ch=input("enter choice")
    if(ch.isdigit()):
        match(int(ch)):
            case 1:
                ca()
                cp()
            case 2:
                ta()
                tp()
            case 3:
                ra()
                rp()
            case 4:
                sa()
                sp()
            case 5:
                print("Thanks for this program")
                break
            case _:
                print("your selection of operation is wrong---try again")
    else:
        print("Don't enter alnums,strs and symbols for int Choice-try again")