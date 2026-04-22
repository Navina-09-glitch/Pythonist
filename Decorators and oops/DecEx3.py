def square(hyd):
    def op():
        n=hyd()
        res=n**2
        return n,res
    return op
@square
def getval():
    return 5
#main program
n,res=getval() #Normal function call
print("Square ({})={}".format(n,res))