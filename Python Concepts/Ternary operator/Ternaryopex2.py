a,b=float(input("enter a:")),float(input("enter b"))
res=a if a>b else b if b>a else "both values are equal"
print("Big({},{})={}".format(a,b,res))