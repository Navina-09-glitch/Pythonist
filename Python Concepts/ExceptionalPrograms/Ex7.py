try:
	print("Program Execution started")
	s1=input("\tEnter Value of a:")
	s2=input("\tEnter Value of b:")
	a=int(s1) #----------------------------ValueError
	b=int(s2) #----------------------------ValueError
	c=a/b  #-------------------------------ZeroDivisionError
	s="PYTHON"
	print("Val=",s[10])
except BaseException:
    print("oooops,something went wrong")
else:
    print("--------------else block-----------------")
    print("\ta=",a)
    print("\tb=",b)
    print("\tDiv=",c)
finally:
    print("\n Iam from finally block")