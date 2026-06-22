def simpleint():
    p=float(input("Enter principle : "))
    t=float(input("Enter time : "))
    r=float(input("Enter rate of interest : "))
    lst=[] #Multiple error
    if(p<=0):
        print("Sorry principle cannot be less than zero")
    if(r<=0):
        print("Sorry rate of interest cannot be greater than zero")
    if(t<=0):
        print("Sorry time cannot be greater than zero")
    if(p<=0) or (r<=0) or (t<=0):
        return"".join(lst)
    else:
        si=(p*t*r)/100
        totamt=p+si
        return p,t,r,t,si,totamt
#Mainprogram
res=simpleint()
if(type(res)==str):
    print(res)
else:
    print("\t\t simple interest calculations")
    print("\tPrincipleamount:{}".format(res[0]))
    print("\tTime:{}".format(res[1]))
    print("\tRate:{}".format(res[2]))
    print("\tSimple Interest:{}".format(res[3]))
    print("\tTotamt:{}".format(res[4]))
