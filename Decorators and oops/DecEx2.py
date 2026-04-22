def getsquare(hyd): #Decorator definition --outer function
    def operation(): #Inner Function
            n=hyd()
            res=n**2
            return n,res
    return operation
def getval():
        return 5
#main program
n,r=getsquare(getval())
print("Square ({})={}".format(n,r))
