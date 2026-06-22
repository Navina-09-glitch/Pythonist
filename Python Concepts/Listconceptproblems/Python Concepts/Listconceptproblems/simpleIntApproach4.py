def simpleint():
    p=float(input("enter principle amount:"))
    t=float(input("enter time :"))
    r=float(input("enter rate :"))
    if(p<=0) or (t<=0) or (r<=0):
        return "Invalid input"
    else:
        si=(p*t*r)/100
        totamt=p+si
        return p,t,r,si,totamt

#Main program
res=simpleint()
if(type(res)==str):
    print(res)
else:
    print("\t\t simple interest calculations")
    print("\t\t Principle amount {}".format(res[0]))
    print("\t\t Time {}".format(res[1]))
    print("\t\t Rate {}".format(res[2]))
    print("\t\t Total amount {}".format(res[4]))
    print("\t\t Simple interest {}".format(res[3]))