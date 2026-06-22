def squareroot(kvr):
    def cal():
        n,sqv=kvr()
        sqrtv=n**0.5
        return n,sqv,sqrtv
    return cal
def square(hyd):
    def op():
        n=hyd()
        res=n**2
        return n,res
    return op

@squareroot
@square
def getval():
    return float(input("Enter a numerical value: "))
#main program
n,sqv,sqrtv=getval() #Normal Function call
print("Square ({})={}".format(n,sqv))
print("Square root ({})={}".format(n,sqrtv))
