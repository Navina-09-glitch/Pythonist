try:
    print("Program Execution Started")
    s1=input("\tEnter value of a:")
    s2=input("\tEnter value of b:")
    a=int(s1)
    b=int(s2)
    c=a/b
    s="PYTHON"
    print("Val=",s[10])
except ZeroDivisionError:
    print("Dont enter zero for Denominator")
except ValueError:
    print("Dont enter alnums,strs and symbols")
except IndexError:
    print("Check the index")
except:
    print("ooops,something went wrong")
else:
    print("\ta=",a)
    print("\tb=",b)
    print("\tDiv=",c)
finally:
    print("\nIam from finally block")