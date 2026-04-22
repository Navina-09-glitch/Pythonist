d=int(input("enter number"))
if(d==0):
    print("{} is zero".format(d))
elif(d==1):
    print("{} is one".format(d))
elif(d==2):
    print("{} is two".format(d))
elif(d==3):
    print("{} is three".format(d))
elif(d==4):
    print("{} is four".format(d))
elif(d==5):
    print("{} is five".format(d))
elif(d==6):
    print("{} is six".format(d))
elif(d==7):
    print("{} is seven".format(d))
elif(d==8):
    print("{} is eight".format(d))
elif(d==9):
    print("{} is nine".format(d))
elif(d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is negative digit".format(d))
elif(d>9):
    print("{} is positive digit".format(d))
elif(d<0) and (d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("{} is negative digit".format(d))

