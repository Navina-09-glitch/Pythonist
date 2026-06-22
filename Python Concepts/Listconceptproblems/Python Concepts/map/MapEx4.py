print("Enter list of Values separated by space:")
tpl=tuple(map(float,input().split()))
print(tpl,type(tpl))
#Find squares by using map with Anonymous Functions
sqrvals=list(map(lambda n:n**2,tpl))
#Find Squareroot by using map with anonymous Functions
sqrtvals=tuple(map(lambda n:n**0.5,tpl))
print("*"*50)
print("GivenValues\t\tSquare Values\t\tSquare roots")
print("*"*50)
for gv,sv,srtv in zip(tpl,sqrvals,sqrtvals):
    print("\t{}\t\t\t{}\t\t\t{}".format(gv,sv,round(srtv,2)))
print("-"*50)