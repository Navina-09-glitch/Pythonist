def area():
    B = float(input("enter base"))
    H = float(input("enter height"))
    area=(1/2)*(B*H)
    print("\t\tArea of Triangle:{}".format(area))
def peri():
    print("Enter three sides values")
    a,b,c=float(input()),float(input()),float(input())
    pt=a+b+c
    print("\t\tPerimeter of Triangle:{}".format(pt))