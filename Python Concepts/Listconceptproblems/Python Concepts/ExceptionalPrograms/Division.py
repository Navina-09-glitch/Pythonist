from excepts import DivisionError
def divop(a,b):
    if(b==0):
        raise DivisionError #Hitting the programmer -defined Exception
    else:
        return (a/b)
