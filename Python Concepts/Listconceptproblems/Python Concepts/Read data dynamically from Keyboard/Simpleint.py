p=float(input("Enter principle amount: "))
t=float(input("Enter time : "))
r=float(input("enter rate of interest:"))
si=(p*t*r)/100
totamt=p+si
print("\t\tPrinciple amount:{}".format(p))
print("\t\tTime:{}".format(t))
print("\t\tRate of interest:{}".format(r))
print("\t\tsimple interest:{}".format(si))
print("\t\tTotal amount:{}".format(totamt))


