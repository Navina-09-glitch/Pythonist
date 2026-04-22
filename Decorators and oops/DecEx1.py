def getsquare(hyd):       #Decorator---outer function
    def operation():      #Inner function
        n=hyd()           #call the original function
        res=n**2          #Square the result
        return n,res      #return both original and result
    return operation      #return the wrapper function

def getval():
    return 5

#main program
op=getsquare(getval)  #Decorator call
n,r=op()
print("Square ({})={}".format(n,r))


#op is object of operation
#waiter, chef
#def waiter(customer):
    #def chef():
        #cv=cum()
        #return cv
    #return chef

