from Figuremenu import menu
from circle import area as ca,peri as cp
from square import area as sa,perimeter as sp
from rect import area as ra,peri as rp
from triangle import area as ta,peri as tp
while(True):
    menu()
    ch=input("Enter your choice:")
    if ch.isdigit():
        match(int(ch)):
            case 1:
                ca()
                cp()
            case 2:
                sa()
                sp()
            case 3:
                ra()
                rp()
            case 4:
                ta()
                tp()
            case 5:
                print("Thanks for using the program")
                break
            case _:
                print("your selection was invalid")
    else:
        print("do not enter alnums,strs and symbols for int choice-try again")


