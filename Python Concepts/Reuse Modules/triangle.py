def area():
    b=float(input("enter base"))
    h=float(input("enter height"))
    area=0.5*b*h
    print("area is {}".format(area))
def peri():
    print("enter 3 sides values")
    a,b,c=float(input()),float(input()),float(input())
    p=(a+b+c)
    print("peri area is {}".format(p))