#icici.py<-----File Name and Module Name
bname="ICICI"
addr="Bangalore-India" # here bname and addr is called global variable names
x=100
def  simpleint(): # Function Definition
    p = float(input("Enter Principle Amount:"))
    t = float(input("Enter Time:"))
    r = float(input("Enter Rate of Interest:"))
    # Cal si and totamt to pay
    si = (p * t * r) / 100
    totamt = p + si
    # display the result
    print("*" * 50)
    print("\t\tPrinciple Amount:{}".format(p))
    print("\t\tTime:{}".format(t))
    print("\t\tRate of Interest:{}".format(r))
    print("\t\tSIMPLE INTEREST:{}".format(si))
    print("\t\tTOTAL AMOUNT TO PAY:{}".format(totamt))
    print("*" * 50)