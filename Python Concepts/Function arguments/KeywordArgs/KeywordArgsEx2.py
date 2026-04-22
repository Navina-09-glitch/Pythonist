def disp(a,b,c,d,city="HYD"):
    print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,city))

#Main Program
print("\tA\tB\tC\tD\tcity")
disp(10,20,30,40)
disp(d=40,a=10,b=20,c=30)
disp(c=30,a=10,b=20,d=40)
disp(10,20,d=40,c=30)
#disp(d=40,c=30,10,20) # Function Call with Pos and Keyword Args--SyntaxError: positional argument follows keyword argument
disp(d=40,c=30,b=20,a=10)
disp(city="MUM",d=40,c=30,b=20,a=10)
disp(10,20,d=40,city="AP",c=30)
