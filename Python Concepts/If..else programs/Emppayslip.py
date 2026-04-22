eno=int(input("Enter Employee number: "))
name=input("Enter employee name: ")
basicsal=int(input("Enter employee basic salary: "))
if(basicsal<=0):
    print("{} invalid salary".format(basicsal))
if(basicsal>10000):
    da=basicsal*(20/100)
    ta=basicsal*(10/100)
    hra=basicsal*(7/100)
    cca=basicsal*(0.5/100)
    ma=basicsal*(0.25/100)
    lic=basicsal*(2/100)
    gpf=basicsal*(1/100)
if(0<basicsal<10000):
    da=basicsal*(15/100)
    ta=basicsal*(7.5/100)
    hra=basicsal*(5/100)
    cca=basicsal*(0.25/100)
    ma=basicsal*(0.12/100)
    lic=basicsal*(1.5/100)
    gpf=basicsal*(1/100)
if(basicsal>0):
    netsal=(basicsal+da+ta+hra+cca+ma)-(lic+gpf)
    print("\t Employee payslip")
    print("\t Employee name:{} ".format(name))
    print("\t employee number:{} ".format(eno))
    print("\t Employee basic salary:{} ".format(basicsal))
    print("\t\t DA:{} ".format(da))
    print("\t\t TA:{} ".format(ta))
    print("\t\t HRA:{} ".format(hra))
    print("\t\t CCA:{} ".format(cca))
    print("\t\t MA:{} ".format(ma))
    print("\t\t LIC:{} ".format(lic))
    print("\t\t GPF:{} ".format(gpf))
    print("\t\t Net salary:{} ".format(netsal))





