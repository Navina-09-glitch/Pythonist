try:
	print("Program Execution started")
	s1=input("\tEnter Value of a:")
	s2=input("\tEnter Value of b:")
	a=int(s1) #----------------------------ValueError
	b=int(s2) #----------------------------ValueError
	c=a/b  #-------------------------------ZeroDivisionError
	s="PYTHON"
	print("Val=",s[10])
except ZeroDivisionError:
	print("Don't enter Zero for Den...") # user-freindly error messages
except ValueError:
	print("Don't enter alnums,strs and symbols")
except IndexError:
	print("Check the Index")
except:
	print("oooops, some this went wrong")
else:
	print("-------------else block-----------------")
	print("\ta=",a)
	print("\tb=",b)
	print("\tDiv=",c)
	print("-------------------------------------------")
finally:
	print("---------------------------------------------")
	print("I am from finally block")