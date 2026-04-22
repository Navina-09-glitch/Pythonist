def cube(blr):
    def perform():
        n,sqv,sqrtv=blr()
        cbtv=n**3
        return n,sqv,sqrtv,cbtv
    return perform

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

@cube
@squareroot
@square
def getval():
    return float(input("Enter a numerical value: "))

#Main Program
n,sqv,sqrtv,cbtv=getval() #Normal Function call
print("Square ({})={}".format(n,sqv))
print("Square root ({})={}".format(n,sqrtv))
print("cube ({})={}".format(n,cbtv))
