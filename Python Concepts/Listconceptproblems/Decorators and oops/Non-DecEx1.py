def getval():
    return 5
def getsquare():
    n=getval()
    sv=n**2
    print("Square({})={}".format(n,sv))
def getsqrtval():
    n=getval()
    sqrtv=n**0.5
    print("Square({})={}".format(n,sqrtv))
def getcube():
    n=getval()
    cv=n**3
    print("Cube({})={}".format(n,cv))

#Main Program
getsquare()
getsqrtval()
getcube()