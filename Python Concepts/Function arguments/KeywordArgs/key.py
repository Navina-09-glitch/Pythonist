def disp(a,b,c,d,city="HYD"):
    print("\t{} \t{} \t {} \t{}".format(a,b,c,d,city))

print("\tA\tB\tC\tD\tcity")
disp(10,20,30,40) #Function call with pos args
disp(d=40,a=10,b=20,c=30) #Function call with keyword args
disp(c=30,a=10,b=20,d=40) #Function call with keyword args
disp(10,20,d=40,c=30) #Function call with pos and keyword args
disp(d=40,c=30,10,20)  #Function call with pos and keyword args ----syntax error: positional argument follows keyword argument
disp(d=40,c=30,b=20,a=10) #Function call with keyword args
disp(city="MUM",d=40,c=30,b=20,a=10) #Function call with keyword args
disp(10,20,d=40,city="AP",c=30) #Function call with Pos and Keyword args