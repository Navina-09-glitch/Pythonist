def disp(a,b,c,d):
    print("\t {} \t {} \t {} \t {}".format(a,b,c,d))

print("\tA\tB\tC\tD")
disp(10,20,30,40) #Function call with positional arguments
disp(d=40,a=10,b=20,c=30) #Function call with keyword args
disp(c=30,a=10,b=20,d=40) #Function call with keyword args
disp(10,20,d=40,c=30) #Function call with POS and keyword args
disp(d=40,c=30,10,20) #Function call with pos and keyword args
#Keyword Args--SyntaxError: positional argument follows keyword argument
It is indicating that always positional arguments must come first then keyword arguments.
disp(d=40,c=30,b=20,a=10) #Function call with keyword args